print("=== Welcome to the Shopping Discount Calculator ===")

while True:
    try:
        
        bill_amount = float(input("\nEnter the total bill amount ($): "))
        discount_percent = float(input("Enter the discount percentage (%): "))

      
        if bill_amount < 0 or discount_percent < 0:
            raise ValueError("Bill amount and discount percentage must be non-negative.")
        
        if discount_percent > 100:
            raise ValueError("Discount percentage cannot exceed 100%.")

    except ValueError as ve:
        
        print(f"\n[Error] Invalid Input: {ve}")
        print("Please enter valid numbers.")

    except Exception as e:
        
        print(f"\n[Error] An unexpected error occurred: {e}")

    else:
       
        discount_amount = (bill_amount * discount_percent) / 100
        final_bill = bill_amount - discount_amount

        print("\n--- Final Bill Summary ---")
        print(f"Original Bill Amount: ${bill_amount:.2f}")
        print(f"Discount Percentage:  {discount_percent}%")
        print(f"Discount Saved:       ${discount_amount:.2f}")
        print(f"Total Payable Amount: ${final_bill:.2f}")
        print("---------------------------")
        
       
        break

    finally:
        print("--> Input processing attempt finished.")