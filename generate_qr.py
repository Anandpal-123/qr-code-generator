import qrcode

# List of contacts
contacts = [
    {
        "name": "Ramesh Roshan",
        "email": "ramesh@example.com",
        "phone": "+91-9876543210",
        "filename": "contact_ramesh.png"
    },
    {
        "name": "Anita Verma",
        "email": "anita@example.com",
        "phone": "+91-9123456789",
        "filename": "contact_anita.png"
    },
    {
        "name": "Rahul Mehta",
        "email": "rahul@example.com",
        "phone": "+91-9988776655",
        "filename": "contact_rahul.png"
    }
]

# Generate and save QR codes with error handling
for contact in contacts:
    try:
        contact_info = f"""
        Name: {contact['name']}
        Email: {contact['email']}
        Phone: {contact['phone']}
        """
        
        # Generate QR code
        qr = qrcode.make(contact_info)
        
        # Save image to file
        qr.save(contact["filename"])
        print(f"✅ QR Code generated and saved as {contact['filename']}")

    except Exception as e:
        print(f"❌ Failed to generate QR Code for {contact['name']}: {e}")