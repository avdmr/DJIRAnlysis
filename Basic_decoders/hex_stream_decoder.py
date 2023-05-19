import datetime

def decode_frame(hex_stream):
    # Perform the decoding logic based on the provided tables and structures
    # Replace the following code with your decoding implementation
    decoded_frame = {
        "Frame Type": hex_stream[0:2],
        "Ver/Length": hex_stream[2:4] + hex_stream[4:6],
        "CmdType": hex_stream[6:8],
        "ENC": hex_stream[8:10],
        "RES": hex_stream[10:12],
        "SEQ": hex_stream[12:14] + hex_stream[14:16],
        "CRC-16": hex_stream[16:18] + hex_stream[18:20],
        "DATA": hex_stream[20:-8],
        "CRC-32": hex_stream[-8:],
    }
    
    return decoded_frame

def process_hex_stream(hex_stream):
    decoded_frame = decode_frame(hex_stream)
    
    # Replace the following code with the desired output logic
    # Print the decoded frame to the terminal
    print("Decoded Frame:")
    for field, value in decoded_frame.items():
        print(f"- {field}: {value}")
    print()

def process_hex_stream_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Create a unique filename based on the current date and time
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file = f"decoded_frames_{timestamp}.txt"

    with open(output_file, 'w') as file:
        for line in lines:
            hex_stream = line.strip()
            decoded_frame = decode_frame(hex_stream)

            # Write the decoded frame to the output file
            file.write("Decoded Frame:\n")
            for field, value in decoded_frame.items():
                file.write(f"- {field}: {value}\n")
            file.write("\n")
    
    print(f"Decoded frames saved to {output_file}")

def main():
    print("Welcome to the Hex Stream Frame Decoder!")

    while True:
        print("Please choose an option:")
        print("1. Input hex stream frame one at a time")
        print("2. Specify a path to a .txt file with hex stream frames")

        option = input("Enter your choice (1 or 2): ")
        
        if option == '1':
            hex_stream = input("Enter the hex stream frame: ")
            process_hex_stream(hex_stream)
            break
        elif option == '2':
            file_path = input("Enter the path to the hex stream file: ")
            process_hex_stream_file(file_path)
            break
        else:
            print("Invalid option. Please try again.\n")

if __name__ == '__main__':
    main()
