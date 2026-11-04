
import tkinter as tk

from interfaces.affiliate_form import AffiliateForm


root = tk.Tk()
root.withdraw()

application = AffiliateForm(root)

root.mainloop()
