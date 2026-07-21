from app.intake.intake_service import IntakeService


bug = IntakeService.create_bug_report(

    title="Login Crash",

    description="Application crashes when password is empty.",

    severity="High",

    file_path="login.py"
)

print(bug)