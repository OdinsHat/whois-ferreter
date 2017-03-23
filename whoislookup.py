import tkinter
from tkinter import ttk
import whois

class WhoisLookup(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.window = parent
        self.init_gui()

    def init_gui(self):
        self.window.title("Domain Whois (Ferreter)")
        self.window.geometry("600x300")
        self.pack(fill="both", padx=10, pady=5)

        ttk.Label(self, text="Domain").pack(pady='5')
        self.domain_entry = ttk.Entry(self, width='290')
        self.domain_entry.pack(padx='5', pady='5')

        self.whois_btn = ttk.Button(self, text="Whois", command=self.fetch_whois)
        self.bind("<Return>", self.fetch_whois)
        self.whois_btn.pack(padx='5', pady='5')

        self.result_text = tkinter.Text(self, width='290', height='100')
        self.result_text.pack(padx='5', pady='5')

    def fetch_whois(self, event = False):
        self.result_text.delete("1.0", tkinter.END)
        url = self.domain_entry.get()
        domain = url.replace('http://', '').replace('www.', '')
        w = whois.query(domain)
        print(w.__dict__)
        result = "Registrar: %s\nCountry: %s\nRegistered: %s\nExpiry: %s\nNameservers: \n%s" % (w.registrar, w.registrant_cc, w.creation_date.__str__(), w.expiration_date.__str__(), '\n'.join(w.name_servers))
        self.result_text.insert(tkinter.END, result)


if __name__ == '__main__':
    window = tkinter.Tk()
    WhoisLookup(window)
    window.mainloop()