import platform
import subprocess

def run_commands():
    system = platform.system()

    if system == 'Windows':
        commands = [
            'python manage.py makemigrations',
            'python manage.py migrate',
            'python manage.py runserver'
        ]
    else:
        commands = [
            'python3 manage.py makemigrations',
            'python3 manage.py migrate',
            'python3 manage.py runserver'
        ]

    for command in commands:
        subprocess.run(command, shell=True)

if __name__ == "__main__":
    run_commands()