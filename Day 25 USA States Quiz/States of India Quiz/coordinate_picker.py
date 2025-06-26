import matplotlib.pyplot as plt
import pandas as pd

# Load the India map
img = plt.imread('India Map.jpeg')  # Make sure the image is in the same directory or provide path

# List of Indian states (you can edit/remove/add more if needed)
states = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand",
    "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur",
    "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab",
    "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura",
    "Uttar Pradesh", "Uttarakhand", "West Bengal", "Delhi", "Jammu and Kashmir",
    "Ladakh", "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli and Daman and Diu",
    "Lakshadweep", "Puducherry"
]

coords = []

fig, ax = plt.subplots()
ax.imshow(img)
plt.title("Click on the map for each state location")

print("\n💡 Click on the image to mark the following state locations:")

def onclick(event):
    ix, iy = int(event.xdata), int(event.ydata)
    state = states[len(coords)]
    print(f"{state}: ({ix}, {iy})")
    coords.append({"state": state, "x": ix, "y": iy})

    if len(coords) == len(states):
        print("\n✅ All coordinates collected!")
        df = pd.DataFrame(coords)
        df.to_csv("india_states.csv", index=False)
        print("📁 Saved to india_states.csv")
        fig.canvas.mpl_disconnect(cid)
        plt.close()

cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()
