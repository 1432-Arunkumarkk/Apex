from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

mail = Flask(__name__)

def send_email(sender_email, receiver_email, cc_email, bcc_email, subject, body, greetings, regards):
    # Your name
    greetings_to = greetings
    regards_to = regards

    # Configurable greeting and closing message with placeholder for the name
    greeting = 'Dear {},'.format(greetings_to)
    regards = 'Regards,\n{}'.format(regards_to)

    # Concatenate the greeting and closing message to the email body
    email_body = greeting + '\n\n' + body + '\n\n' + regards

    # Create a MIMEText object for the email body
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = ', '.join(receiver_email) if receiver_email else None
    message['Cc'] = ', '.join(cc_email) if cc_email else None
    message['Bcc'] = ', '.join(bcc_email) if bcc_email else None
    message['Subject'] = subject
    message.attach(MIMEText(email_body, 'html'))

    # SMTP server configuration
    smtp_server = 'smtp.zoho.in'
    smtp_port = 587  # Use 587 for STARTTLS

    # Zoho Mail credentials
    username = 'intalert@integramicro.co.in'
    password = 'tEi99nTr@'

    try:
        # Establish a connection to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Enable TLS encryption

        # Login to the SMTP server
        server.login(username, password)

        # Combine all recipient email addresses (To, CC, BCC)
        all_recipients = []
        if receiver_email:
            all_recipients.extend(receiver_email)
        if cc_email:
            all_recipients.extend(cc_email)
        if bcc_email:
            all_recipients.extend(bcc_email)
        # Send the email
        print(all_recipients)
        server.sendmail(sender_email, all_recipients, message.as_string())
        

        # Close the connection
        server.quit()

        return True, None  # Email sent successfully
    except Exception as e:
        return False, str(e)  # Error occurred while sending email

@mail.route('/send_email', methods=['POST'])
def api_send_email():
    data = request.json
    sender_email = data.get('sender_email')
    receiver_email = data.get('receiver_email')
    bcc_email = data.get('bcc_email', [])
    cc_email = data.get('cc_email', [])
    subject = data.get('subject')
    body = data.get('body')
    greetings = data.get('greetings_to')
    regards = data.get('regards_from')

    if not sender_email or not subject or not body:
        return jsonify({'success': False, 'message': 'Missing required fields'}), 400

    success, error = send_email(sender_email, receiver_email, cc_email, bcc_email, subject, body, greetings, regards)
    if success:
        return jsonify({'success': True, 'message': 'Email sent successfully'}), 200
    else:
        return jsonify({'success': False, 'message': 'Failed to send email', 'error': error}), 500

if __name__ == '__main__':
    mail.run(host='10.10.30.37', port='5001', debug=True)
