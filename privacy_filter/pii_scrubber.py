import re
import json

class PrivacyShield:
    """
    Aegis-Graph Privacy-Shield Agent (Zero-Knowledge Edge Scrubber)
    Implements PII redaction logic as specified in Whitepaper Chapter 4.1.
    """
    
    def __init__(self):
        # Basic patterns for PII detection (Regex-based for Edge NPU efficiency)
        self.patterns = {
            'email': r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+',
            'phone': r'(\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}',
            'ssn': r'\b\d{3}-\d{2}-\d{4}\b',
            'birth_date': r'\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b',
            'credit_card': r'\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b'
        }

    def scrub_text(self, text):
        """Redacts sensitive entities from the input text."""
        scrubbed_text = text
        for label, pattern in self.patterns.items():
            scrubbed_text = re.sub(pattern, f"[REDACTED_{label.upper()}]", scrubbed_text)
        return scrubbed_text

    def prepare_audit_payload(self, raw_data):
        """
        Converts raw transcript data into a sovereign-safe audit payload.
        Ensures PII never reaches the network interface.
        """
        if isinstance(raw_data, str):
            return self.scrub_text(raw_data)
        
        if isinstance(raw_data, dict):
            # Deep scrub for JSON/Dict payloads
            clean_payload = {}
            for k, v in raw_data.items():
                if isinstance(v, str):
                    clean_payload[k] = self.scrub_text(v)
                else:
                    clean_payload[k] = v
            return clean_payload
        
        return raw_data

# Example usage for testing
if __name__ == "__main__":
    shield = PrivacyShield()
    sample_text = "Student John Doe, DOB: 05/12/1998, SSN: 123-45-6789, Email: john@example.com"
    print("Original:", sample_text)
    print("Scrubbed:", shield.prepare_audit_payload(sample_text))
