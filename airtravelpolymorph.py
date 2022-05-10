"""Model for FLight and aircraft class"""


class Flight:

    """Model for flight with particular aircraft"""
    
    def __init__(self,number,aircraft):
        if not number[:2].isalpha():
            raise ValueError(f"No airline code in '{number}'")
        
        if not number[:2].isupper():
            raise ValueError(f"Invalid airline code'{number}'")
        
        if not (number[2:].isdigit() and int(number[2:])<= 9999):
           raise ValueError(f"Invalid route number '{number}'")
        
        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def aircraft_model(self):
        return self._aircraft.model()
    
    
    def number(self):
        return self._number
    
    def airline(self):
        return self._number[:2]

    def allocate(self,seat, passenger):
        """ Allocate seat to a passenger"""
        rows,seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError(f"Invalid seat letter {letter}")

        row_text = seat[:-1]
        try:
           row=int(row_text)
        except:
            raise ValueError(f"Invalid seat row{row_text}")
      
        if row not in rows:
            raise ValueError(f"InValid row number {row}")

        if self._seating[row][letter] is not None:
            raise ValueError(f"Seat {seat} already occupied")

        self._seating[row][letter] = passenger

     
    def _parse_seat(self, seat):
         rows, seat_letters = self._aircraft.seating_plan()

         letter = seat[-1]
         if letter not in seat_letters:
             raise ValueError(f"Invalid seat {letter}")

         row_text = seat[:-1]
         try:
             row=int(row_text)
         except ValueError:
             raise ValueError(f"Invalid seat row {row_text}")

         if row not in rows:
             raise ValueError(f"Invalid row number{row}")

         return row, letter

    def relocate_passenger(self, from_seat, to_seat):
         """Relocate passenger to a siff seat """
         from_row, from_letter = self._parse_seat(from_seat)
         if self._seating[from_row][from_letter] is None:
             raise ValueError(f"No passenger to relocate in seat {from_seat}")
         
         to_row,to_letter = self._parse_seat(to_seat)
         if self._seating[to_row][to_letter] is not None:
             raise ValueError(f"Seat {to_seat} already occupied")

         self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
         self._seating[from_row][from_letter] = None
      
    def num_available_seats(self):
        return sum(sum(1 for s in row.values() if s is None)
                   for row in self._seating
                   if row is not None)
    
    def make_boarding_cards(self, card_printer):
        for passenger, seat in sorted(self._passenger_seats()):
            card_printer(passenger,seat, self.number(),self.aircraft_model())

    def _passenger_seats(self):
        """Iterable series of passenger locations"""
        row_numbers,seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                   yield(passenger,f"{row}{letter}")




class Aircraft:
    
    def __init__(self,registration):
        self._registration = registration

    def registration(self):
        return self._registration

    def num_seats(self):
        rows, row_seats = self.seating_plan()
        return len(rows) * len(row_seats)





class AirbusA319(Aircraft):

    def model(self):
        return "Airbus A319"
    
    def seating_plan(self):
        return range(1,23), "ABCDEF"




class Boeing777(Aircraft):


    def model(self):
        return "Boeing 777"
    
    def seating_plan(self):
        return range(1,56) , "ABCDEGHJK"


    

##class Aircraft:
##    def __init__(self,registration,model,num_rows,num_seats_per_row):
##        self._registration = registration
##        self._model = model
##        self._num_rows = num_rows
##        self._num_seats_per_row = num_seats_per_row

##    def registration(self):
##        return self._registration 
    
##    def model(self):
##        return self._model

##    def seating_plan(self):
##        return (range(1, self._num_rows +1),"ABCDEFGHIJK"[:self._num_seats_per_row])


def console_card_printer(passenger,seat,flight_number,aircraft):
    output = f"|Name: {passenger}" \
             f" Flight: {flight_number}" \
             f" Seat: {seat}" \
             f" Aircraft: {aircraft}" \
             "|"
     
    banner = "+"+ "-" * (len(output)-2)+ "+"
    border = "|" +" " *(len(output)-2) + "|"
    lines = [banner,border,output,border,banner]
    card = "\n".join(lines)
    print(card)
    print()



def make_flight():
    f = Flight("BA756",Aircraft("E-890","Airbus A340", num_rows=22,num_seats_per_row=6))
    f.allocate("12A","Ross")
    f.allocate("12B", "Remi")
    f.allocate("15F", "Bjarne")
    f.allocate("13C", "JohnMcCarthy")
    return f

    # pass
