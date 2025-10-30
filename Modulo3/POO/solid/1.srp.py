# Single Responsibility Principle (SRP)

class Report:
    def __init__(self, title, content, extention, user):
        self.title = title
        self.content = content
        self.extention = extention
        self.user = user
        
    def perform(self):
        self.generate_report()
        self.send_email()

    def generate_report(self):
        if self.extention == 'txt':
            return self._generate_txt()
        elif self.extention == 'pdf':
            return self._generate_pdf()
        else:
            return self._generate_default()

    def _generate_txt(self):
         print(f"Generating TXT report for {self.user}:\n{self.title}\n\n{self.content}")

    def _generate_pdf(self):
         print(f"Generating PDF report for {self.user}:\n{self.title}\n\n{self.content}")

    def _generate_default(self):
         print(f"Generating DEFAULT report for {self.user}:\n{self.title}\n\n{self.content}")

    def send_email(self):
        print(f"Sending report '{self.title}' to {self.user} via email.")
      
# Ejemplo de uso
report = Report("Monthly Sales", "Sales data for the month...", "pdf", "user@example.com")
report.perform()
