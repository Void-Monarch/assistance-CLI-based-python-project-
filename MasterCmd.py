from rich import print as cprint
import speech_recognition as sr


class MasterCmd:

    def __init__(self,):
        cprint("[bold red][+][/bold red] [bold orange]Entered into master mode!![/bold orange]")

        self.queryProcess

    def exit(self,query):
        cprint(f"[red][++] Terminating Assistant as per Master code: [/red] [purple]{query}[/purple]")
        exit(0)



    def takeCommand(self):
        """
        To listen , and take input via voice
        :return:
        """
        r = sr.Recognizer()
        with sr.Microphone() as source:
            cprint("\n[blue][+][/blue] [italic magenta]Listening... [red][**]Master Mode[/red] [/italic magenta]\n")
            r.pause_threshold = 0.8
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-us')
            cprint(f"[italic yellow]\tuser said[/italic yellow] [pink]{query}[/pink]")

            return query.lower()
        except Exception as e:
            # print(e)
            cprint("[red][-] Say that again please ...[red] ")
            return "None"

    @property
    def queryProcess(self):
        query = self.takeCommand()

        if query == "exit all" or query == "kill all":
            self.exit(query)

        if query == "exit now" or query == "kill now":
            return "reset"


