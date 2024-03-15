# Initial list of states
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia",
                     "Arkansas", "Michigan", "Connecticut", "South Carolina", 
                     "New Hampshire", "Virginia", "New York", "Massachusetts", 
                     "Maryland", "North Carolina", "Rhode Island", "Mississippi", 
                     "Illinois", "North Dakota", "Vermont", "Alabama", "Maine",
                     "Kentucky", "Tennessee", "Missouri", "Ohio", "Louisiana", 
                     "Indiana", "Florida", "Texas", "Iowa", "Idaho", "Wisconsin", 
                     "California", "Minnesota", "Oregon", "Kansas", "Nevada", 
                     "Nebraska", "Colorado", "North Dakota", "South Dakota", 
                     "Montana", "Utah", "Oklahoma", "New Mexico", "Arizona", 
                     "West Virginia", "Washington", "Wyoming", "Alaska", "Hawaii"]

# Display the length of the list
print("Length of the list:", len(states_of_america))

# Append "Puerto Rico" to the list
states_of_america.append("Puerto Rico")
print("Appended Puerto Rico to the list.")

# Insert "District of Columbia" at the beginning of the list
states_of_america.insert(0, "District of Columbia")
print("Inserted District of Columbia at the beginning of the list.")

# Remove "Hawaii" from the list
states_of_america.remove("Hawaii")
print("Removed Hawaii from the list.")

# Pop the last element from the list
popped_state = states_of_america.pop()
print("Popped state from the list:", popped_state)

# Get the index of "Texas" in the list
index_texas = states_of_america.index("Texas")
print("Index of Texas in the list:", index_texas)

# Count occurrences of "Texas" in the list
count_texas = states_of_america.count("Texas")
print("Number of occurrences of Texas in the list:", count_texas)

# Sort the list
states_of_america.sort()
print("Sorted list (first 5 elements):", states_of_america[:5])

# Reverse the list
states_of_america.reverse()
print("Reversed list (first 5 elements):", states_of_america[:5])

# Clear the list
states_of_america.clear()
print("Cleared the list.")

# Final state of the list
print("Final state of the list:", states_of_america)
