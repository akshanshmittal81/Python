is_boiling=True
stri_count=5
total_actions=stri_count+is_boiling#upcasting
print(f"total actions taken{total_actions}")

milk_present=None#no milk
print(f"Is there milk? {bool(milk_present)}")


water_hot=True
tea_added=False

can_server =water_hot and tea_added
print(f"Can serve chai?{ can_server}")