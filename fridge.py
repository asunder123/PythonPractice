"""Demonstrate raiding"""
from contextlib import closing

class RefrigeratorRaider:
     """Raid a fridge"""
     def open(self):
         print("Open fridge")
     
     def take(self,food):
         print(f"Finding {food}...")
         if food == 'deep fried stuff':
            raise RunTimeError("HealthWarning")
         print(f"Taking{food}")

     def close(self):
         print("Close fridge")

def raid(food):
     with closing(RefrigeratorRaider()) as r:
         r = RefrigeratorRaider()
         r.open()
         r.take(food)
