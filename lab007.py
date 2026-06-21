import csv

# Lab 007: Fault-Tolerant CSV Scanner
# This list resides in the Stack (reference) pointing to dynamic Dict objects in the Heap.
scanned_results = []

print("--- Lab 007: Fault-Tolerant CSV Scanner Activated ---")
print("Type 'exit' at any prompt to terminate input and save to CSV.\n")

while True:
    # 1. Capture and sanitize Student Name
    name_input = input("Enter Student Name: ").strip()
    if name_input.lower() == 'exit':
        break
    if not name_input:
        print("[!] Validation Error: Name cannot be empty. Re-trying loop...")
        continue

    # 2. Fault-Tolerant Block for Numeric Scores
    try:
        score_raw = input(f"Enter {name_input}'s Cyber Security Score (0-100): ").strip()
        if score_raw.lower() == 'exit':
            break
            
        # This conversion will throw a ValueError instantly if string is non-numeric (e.g., 'xyz')
        score = float(score_raw)
        
        # Range validation constraint
        if score < 0 or score > 100:
            print("[!] Validation Error: Score must be between 0 and 100.")
            continue

    except ValueError:
        # Crucial Boundary: Catches 'xyz', stack reference is preserved, heap memory is safe.
        print("[!] Memory Guard: Invalid numeric input detected! Skipping this corrupted record.")
        continue

    # 3. Successful Validation: Appending structured dict object to the Heap memory
    student_record = {
        "Name": name_input,
        "Score": score
    }
    scanned_results.append(student_record)
    print(f"[+] Record staged successfully for {name_input}.\n")

# --- Post-Loop Execution: Writing Staged Records to a CSV File ---
print(f"\n--- Processing {len(scanned_results)} Staged Records ---")

if scanned_results:
    csv_filename = "lab007_student_report.csv"
    
    # Writing safely using standard context manager
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ["Name", "Score"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerows(scanned_results)
        
    print(f"[✔] Mission Success! Records safely pushed to permanent storage: '{csv_filename}'")
else:
    print("[!] Execution Aborted: No valid records were committed to memory.")
