from cx_Freeze import setup,Executable
setup(name="Send Messag",
      version="2.0",
      author="BOX",
      description="You can send mail using this program",
      executables=[Executable(r"send_messag_via_mail2.py",
                   icon=r"Email.ico",
                   shortcutName="Send Mail",
                   shortcutDir="DesktopFolder")]
    )
