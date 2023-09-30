import requests
from dotenv import load_dotenv
import os
from tkinter import *


def get_conversion(from_currency, to_currency, amount):
    """
    This function fetches the data from API and returns the response

    arguments:
    from_currency -- The currency code of source currency. Example 'USD' for US Dollars or 'INR' for Indian R
    to_currency -- The currency code of destination currency. Example 'NPR' for Nepali Rupees
    amount -- The amount to convert from the source currency to the destination currency

    return:
    response -- Returns a float with the appropriate converted amount 
    """
    load_dotenv()
    url = "https://currency-exchange.p.rapidapi.com/exchange"

    querystring = {"from":from_currency,"to":to_currency}

    headers = {
    	"X-RapidAPI-Key": os.getenv("MY_API_KEY"),
    	"X-RapidAPI-Host": "currency-exchange.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)

    return response.json()*amount


def display_converted_amount(from_currency, to_currency,amount,label):
    """
    This function is used to call the conversion function which further makes a call to the API, get the data and then display it to the GUI Label
    """
    result_string = f"{amount} {from_currency} = {get_conversion(from_currency, to_currency,amount)} {to_currency}"
    label.config(text=result_string)


# The driver code for the program
if __name__ == '__main__':
    window = Tk()

    full = Frame(window, bg="#4d4646")
    full.pack(expand=True, fill=BOTH)

    # Label
    lbl = Label(full, text="Currency Conversion !", fg='#4d4646',
                bg="#7fcd91", font=("montserrat", 20))
    lbl.pack(expand=True, fill=X, ipady=25)

    input_areas = Canvas(full,bg="#4d4646",borderwidth=0, border=0)

    from_currency = Label(input_areas, text="From Currency:", bg="#4d4646", fg="#7fcd91", font=("montserrat",14))
    from_currency_input = Entry(input_areas, font=("montserrat",14))
    from_currency_input.config(justify="center")

    
    amount = Label(input_areas, text="Amount:", bg="#4d4646", fg="#7fcd91", font=("montserrat",14))
    amount_input = Entry(input_areas, font=("montserrat",14))
    amount_input.config(justify="center")

    to_currency = Label(input_areas, text="To Currency:", bg="#4d4646", fg="#7fcd91", font=("montserrat",14))
    to_currency_input = Entry(input_areas, font=("montserrat",14))
    to_currency_input.config(justify="center")


    from_currency_input.insert(0, "USD")
    amount_input.insert(0, "1")
    to_currency_input.insert(0, "NPR")

    
    from_currency.grid(row=0, column=0, ipady=10, padx=60)
    from_currency_input.grid(row=1, column=0, ipady=10, padx=100)
    
    amount.grid(row=2, column=0, ipady=10, padx=60)
    amount_input.grid(row=3, column=0, ipady=10, padx=100)


    to_currency.grid(row=4, column=0, ipady=10, padx=60)
    to_currency_input.grid(row=5, column=0, ipady=10, padx=100)

    result = Label(full, text="", bg="#4d4646", fg="#7fcd91", font=("montserrat",14))

    btn_convert_currency = Button(full, text="Convert", bg='#7fcd91', fg="#5b5656", font=(
        "Montserrat", 14), activebackground="black", activeforeground="#7fcd91", command=lambda:display_converted_amount(from_currency=from_currency_input.get(), to_currency=to_currency_input.get(), amount=float(amount_input.get()),label=result))
    
    input_areas.pack(expand=True, fill=X)
    btn_convert_currency.pack(expand=True, ipadx=30, ipady=10)
    
    result.pack(expand=True, fill=X)

    window.title('Currency Today')
    window.geometry("500x600+10+20")
    window.mainloop()

