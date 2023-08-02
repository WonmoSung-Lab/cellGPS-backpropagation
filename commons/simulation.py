import numpy as np

class AnnihilationEvent:
    def __init__(self, location, direction, time):
        self.location = location
        self.direction = direction
        self.time = time
        
class ScannerCylinder:
    def __init__(self, length, diameter):
        self.length = length
        self.diameter = diameter
        
    def get_LOR(self, events):
        radius = self.diameter / 2
        LORs = []
        for event in events:
            x, y, z = event.location
            a, b, c = event.direction
            
            k1 = (- z*c - y*b + np.sqrt( (z*c + y*b)**2 - (b**2 + c**2)*((y*z)**2 - radius**2 )))/(b**2 + c**2)
            k2 = (- z*c - y*b - np.sqrt( (z*c + y*b)**2 - (b**2 + c**2)*((y*z)**2 - radius**2 )))/(b**2 + c**2)
            
            Response1 = np.array(event.location) + k1 * np.array(event.direction)
            Response2 = np.array(event.location) + k2 * np.array(event.direction)
            
            Response1 = Response1.tolist()
            Response2 = Response2.tolist()
            
            if np.abs(Response1[0]) <= self.length / 2 and np.abs(Response2[0]) <= self.length / 2:
                norm = np.linalg.norm(np.array(Response1))
                Response1.append(event.time + norm / 3e8)
                norm = np.linalg.norm(np.array(Response2))
                Response2.append(event.time + norm / 3e8)
                LORs.append(Response1 + Response2)
    
        return LORs

class ScannerLine:
    def __init__(self, length, height):
        self.length = length
        self.height = height
        
    def get_LOR(self, events):
        LORs = []
        for event in events:
            x, y = event.location
            a, b = event.direction
            if a < 0:
                a = -a
                b = -b
                
            upResponse = [x + a * (self.height / 2 - y) / b, self.height / 2]
            downResponse = [x - a * (self.height / 2 + y) / b, - self.height / 2]
            
            if np.abs(upResponse[0]) <= self.length / 2 and np.abs(downResponse[0]) <= self.length / 2:
                norm = np.linalg.norm(np.array(upResponse))
                upResponse.append(event.time + norm / 3e8)
                norm = np.linalg.norm(np.array(downResponse))
                downResponse.append(event.time + norm / 3e8)
                LORs.append(upResponse + downResponse)
        
        return LORs
        
#     def get_exact_response(self, events):
#         Responses = []
#         for event in events:
#             x = event.location[0]
#             a, b = event.direction
#             if a < 0:
#                 a = -a
#                 b = -b
                
#             upResponse = [x + a * (self.height / 2 - y) / b, self.height / 2]
#             if np.abs(upResponse[0]) <= self.length / 2:
#                 norm = np.linalg.norm(np.array(upResponse))
#                 upResponse.append(event.time + norm / 3e8)
#                 Responses.append(upResponse)

#             downResponse = [x - a * (self.height / 2 + y) / b, - self.height / 2]
#             if np.abs(downResponse[0]) <= self.length / 2:
#                 norm = np.linalg.norm(np.array(downResponse))
#                 downResponse.append(event.time + norm / 3e8)
#                 Responses.append(downResponse)
    
#         return Responses

class Track:
    def __init__(self, function, dimension):
        self.function = function
        self.dimension = dimension
    
    def generate_events(self, t0, t1, dt):
        timestamps = np.arange(t0, t1, dt)
        events = []
        for time in timestamps:
            location = self.function(time) #+ np.random.randn(self.dimension) / 5
            direction = np.random.randn(self.dimension)
            events.append(AnnihilationEvent(location, direction, time))
        return events