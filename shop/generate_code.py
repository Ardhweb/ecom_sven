import uuid

class UID_CODE_Generator:
    def __init__(self):
        self.uuid = uuid.uuid4()

    def generate_hex(self,limit):
        """Generates and returns the UUID in hexadecimal format."""
        return self.uuid.hex[:limit]

    def generate_int(self,limit):
        """Generates and returns the UUID in integer format."""
        self.limit = limit
        int_code = self.uuid.int
        return str(int_code)[:limit]

    def get_code(self,format="hex",limit=None):
       
        if format == "hex":
            return self.generate_hex(8)
        elif format == "int":
            return self.generate_int(limit)
        else:
            raise ValueError(f"Invalid format: {format}")

code_request = UID_CODE_Generator()

# print(f"Hex Code:{x.get_code('hex', 1)}, Int Code:{x.get_code('int',4)}")

# print(x.get_code('hex', 1))
# print(x.get_code('int',4))