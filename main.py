import struct
import os

class LiteDB7:
    def __init__(self, filename="data.bin"):
        self.filename = filename
        # Format: 'I' (unsigned int for key) and '16s' (16-byte string for value)
        self.record_format = "<I16s" 
        self.record_size = struct.calcsize(self.record_format)

    def put(self, key, value):
        """Saves a key and value into the binary file."""
        # Ensure value is exactly 16 bytes
        value_bytes = value.encode('utf-8')[:16].ljust(16, b'\x00')
        packed_data = struct.pack(self.record_format, key, value_bytes)
        
        with open(self.filename, "ab") as f:
            f.write(packed_data)
        print(f"Stored: Key={key}, Value={value}")

    def get(self, search_key):
        """Searches the binary file for a specific key."""
        if not os.path.exists(self.filename):
            return None
            
        with open(self.filename, "rb") as f:
            while True:
                chunk = f.read(self.record_size)
                if not chunk:
                    break
                key, value = struct.unpack(self.record_format, chunk)
                if key == search_key:
                    return value.decode('utf-8').strip('\x00')
        return None

# --- TEST IT ON YOUR WINDOWS 7 MACHINE ---
db = LiteDB7()
db.put(101, "User_Samar")
db.put(344, "AIR_Rank")

result = db.get(344)
print(f"Retrieved from Disk: {result}")