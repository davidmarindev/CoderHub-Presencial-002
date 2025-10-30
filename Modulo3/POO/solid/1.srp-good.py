# Single Responsibility Principle (SRP)

class Report:
    def __init__(self, title, content, extention, user):
        self.title = title
        self.content = content
        self.extention = extention
        self.user = user
        
    def perform(self):
        generator = ReportGenerator(self.title, self.content, self.extention)
        report = generator.generate()
        sender = EmailSender(self.user)
        sender.send(report)

class ReportGenerator:
    def __init__(self, title, content, extention):
        self.title = title
        self.content = content
        self.extention = extention

    def generate(self):
        if self.extention == 'txt':
            return self._generate_txt()
        elif self.extention == 'pdf':
            return self._generate_pdf()
        else:
            return self._generate_default()

    def _generate_txt(self):
         print(f"Generating TXT report:\n{self.title}\n\n{self.content}")

    def _generate_pdf(self):
         print(f"Generating PDF report:\n{self.title}\n\n{self.content}")

    def _generate_default(self):
         print(f"Generating DEFAULT report:\n{self.title}\n\n{self.content}")
         
class EmailSender:
    def __init__(self, user):
        self.user = user

    def send(self, report):
        print(f"Sending report '{report.title}' to {self.user} via email.")