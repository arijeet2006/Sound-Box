Django Droid Sound Box is an IoT-style project that turns an Android device into a remote-controlled sound server. By combining a Django web backend with DroidRun for mobile automation, this project allows users to trigger physical audio playback on a phone via a web interface.

📺 Demo
https://www.linkedin.com/posts/arijeet-das-2a80b5329_droidrun-django-androiddevelopment-activity-7419110368431644672-agqh?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFLGLmABYikbWoaWL2mcsxb0ZW_ob60KWGw

🚀 How It Works
The Backend (Django): Hosts a web interface with buttons/triggers. When a user clicks a button, the server queues a command or exposes an API endpoint.
The Client (DroidRun): Running on an Android device, the DroidRun script continuously listens to the Django server.
The Action: When the script detects a trigger from the server, it commands the Android OS to play the specific audio file through the device speakers.

🛠️ Tech Stack
Backend: Python, Django
Mobile Automation: DroidRun
Frontend: HTML/CSS (Simple control dashboard)
Hardware: Any Android Smartphone

📂 Project Structure
Bash

├── django_server/       # The Django project files
│   ├── manage.py
│   ├── soundbox_app/    # Main app logic
│   └── static/          # CSS/JS for the dashboard
├── droidrun_script/     # The script running on the phone
│   └── client.py        # Listens to server and plays audio
├── sounds/              # Audio files (mp3/wav)
└── README.md
