import time

# Example actions dictionary
actions = {
    1: "Akcja 1",
    2: "Akcja 2",
    3: "Akcja 3"
}

def generate_and_update_code(selected_action):
    """
    Generates and prints code for the given action.
    """
    # Check if the selected action exists in actions dictionary
    if selected_action not in actions:
        print(f"❌ Akcja o numerze {selected_action} nie istnieje.")
        return
    
    # Generate code dynamically
    generated_code = f"""
# Kod dla akcji: {selected_action}
def action_{selected_action}():
    print("Uruchamianie akcji: {actions[selected_action]}")
action_{selected_action}()
"""
    print("📜 Wygenerowany kod:\n")
    print(generated_code)
    print("🎮 Aktualizacja zakończona!\n")

def continuous_code_generation(iterations=5):
    """
    Manages multiple iterations of code generation and updates.
    """
    print("🚀 Rozpoczynam dynamiczne generowanie kodów...\n")
    for i in range(iterations):
        print(f"🔄 Iteracja {i + 1}:")
        
        # Example: Automatically select an action (cycles through available actions)
        selected_action = (i % len(actions)) + 1
        generate_and_update_code(selected_action)
        time.sleep(2)  # Simulate processing time

    print("\n🎮 Wszystkie procesy zakończone pomyślnie! 🔥♾️")

# Main entry point
if __name__ == "__main__":
    continuous_code_generation()