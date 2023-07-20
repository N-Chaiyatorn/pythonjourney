class RainDetector():
    
    def detecting(self, i):
        if i['weather'][0]['id'] >= 500 and i['weather'][0]['id'] < 600:
            return True
        else:
            return False
        
    def display_the_result(self, hours):
        print(f"\nIn {hours} rain will occur.\n")