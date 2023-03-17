import typer

app = typer.Typer()

class Garage():
    def __init__(self, tickets: list, spaces: int, current_tickets: dict = {}):
        self.tickets = tickets
        self.spaces = spaces
        self.current_tickets = current_tickets

    @app.command()
    def main(self):
        while True:
            choice = input('type "add | show | leave | exit": ')
            if choice.lower() == "exit":
                break
            elif choice.lower() == "add":
                self.add_ticket()
            elif choice.lower() == "show":
                self.show_tickets()
            elif choice.lower() == "leave":
                self.leave()
            else:
                print("please choose a valid option, or 'exit' to quit.")

    @app.command()
    def add_ticket(self):
        self.spaces -= 1
        ticket_num = self.tickets.pop()
        self.current_tickets[ticket_num] = "unpaid"
        print(f"ticket { ticket_num } added")

    @app.command()
    def show_tickets(self):
        print(f'Tickets left: { self.spaces }')
        print(self.current_tickets)

    @app.command()
    def leave(self):
        number = input('What was your ticket number?')
        if int(number) not in self.current_tickets:
            print('Did not check out')
        else: 
            self.spaces += 1
            self.tickets.append(number)
            print('thanks bye')
    

@app.command()
def run():
    my_garage = Garage([i for i in range(1,11)], 10, {})
    my_garage.main()

