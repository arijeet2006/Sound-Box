from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Sum
from .models import PaymentLog
import json


def dashboard(request):

    total = PaymentLog.objects.aggregate(Sum('amount'))['amount__sum'] or 0.00
   
    recent = PaymentLog.objects.order_by('-timestamp')[:5]

    context = {
        'total_amount': total,
        'recent_payments': recent
    }
    return render(request, 'index.html', context)

@csrf_exempt
def log_payment(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
          
            PaymentLog.objects.create(
                sender=data.get('sender', 'Unknown'),
                amount=data.get('amount', 0.0)
            )
            return JsonResponse({'status': 'success', 'message': 'Payment Saved'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
            
    return JsonResponse({'status': 'failed', 'message': 'Only POST allowed'})

def get_live_data(request):

    total = PaymentLog.objects.aggregate(Sum('amount'))['amount__sum'] or 0.00
    
    latest = PaymentLog.objects.order_by('-timestamp').first()
    
    data = {
        'total_amount': total,
        'latest_sender': latest.sender if latest else "No Data",
        'latest_amount': latest.amount if latest else 0,
        'latest_timestamp': latest.timestamp.strftime("%H:%M:%S") if latest else ""
    }
    return JsonResponse(data)