import matplotlib.pyplot as plt

# Create figure and axes
fig, ax = plt.subplots()

# Header
ax.text(0, 0.8, 'Ian Dover:\n', fontsize = 20, ha = 'center', va = 'center')
ax.text(0, 0.8, 'Topics on High Dimensional Data Analytics:\n', fontsize = 20, ha = 'center', va = 'center')
ax.text(0, 0.8, '02/03/23\n', fontsize = 20, ha = 'center', va = 'center')

# # Paragraph 1
# ax.text(0, 0.8, "Paragraph 1:\n", fontsize = 20, ha = 'left', va = 'center')
# ax.text(0, 0.6, "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque commodo, nisi a scelerisque facilisis, leo est convallis quam, vel auctor diam lectus vel velit. Aenean vel augue id ipsum hendrerit condimentum ut at erat. Integer in tortor quam.", fontsize=15, ha='left', va='center')

# # Image
# image = plt.imread("example_image.jpg")
# ax.imshow(image)
# ax.text(0.5, -0.1, "Example Image", ha='center', va='center', transform=ax.transAxes, fontsize=15)

# # Paragraph 2
# ax.text(0, -0.5, "Paragraph 2:\n", fontsize=20, ha='left', va='center')
# ax.text(0, -0.7, "Aliquam rutrum, dui ac tristique posuere, est nulla pulvinar metus, in dapibus sapien odio id diam. Nunc auctor, dolor eget bibendum condimentum, sapien ligula malesuada metus, euismod pharetra sem magna id dui. In auctor commodo neque, in semper lacus tincidunt eget.", fontsize=15, ha='left', va='center')

# Remove axis
ax.axis('off')

# Save the report
plt.savefig('assignment2.pdf', bbox_inches='tight')