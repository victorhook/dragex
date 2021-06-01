from protocol.packet import Packet


class Connection:

    def open(self) -> bool:
        pass

    def close(self) -> bool:
        pass

    def send(self, packet: Packet) -> bool:
        pass

    def read(self) -> Packet:
        pass
