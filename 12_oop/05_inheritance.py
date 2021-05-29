"""
    AUTHOR: GAUTAM CHANDRA SAHA
    DATE & TIME: 29/05/21 AT 11:01 PM

"""


class Device:

    def __init__(self, is_connected, device, connected_via):
        self.is_connected = is_connected
        self.device = device
        self.connected_via = connected_via

    def disconnect(self):
        self.is_connected = False
        print(f"{self.device} disconnected!")


class Camera(Device):
    def __init__(self, is_connected, device, connected_via, memory, shots):
        super().__init__(is_connected, device, connected_via)
        self.shots = shots
        self.capacity = memory

    def capture(self):
        if self.is_connected:
            print(f"Taking {self.shots} shots")
            print(self.remaining_shots())
        else:
            print(f"{self.device} not connected!")

    def remaining_shots(self):
        return f"Remaining shots {self.capacity - self.shots}"


def main():
    nikon11x = Camera(True, "Nikon", "wifi", 500, 50)
    nikon11x.capture()
    nikon11x.disconnect()


if __name__ == '__main__':
    main()
