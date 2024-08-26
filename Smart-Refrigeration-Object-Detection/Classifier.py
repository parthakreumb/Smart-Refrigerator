def class_pred(model, img_url, base_name, img_shape, imagenet_labels):
  img2 = tf.keras.utils.get_file('img',img_url)
  img = Image.open(img2).resize(img_shape)

  img = np.array(img)/255.0
  
  result = model.predict(img[np.newaxis, ...])
  predicted_class = np.argmax(result[0], axis=-1)
  predicted_class_name = imagenet_labels[predicted_class]
  
  
  plt.imshow(img)
  plt.axis('off')
  predicted_class_name = imagenet_labels[predicted_class]
  _ = plt.title("Prediction: " + predicted_class_name.title())
  

  
img_url = "https://upload.wikimedia.org/wikipedia/commons/1/11/Tomato_%283667951881%29.jpg"
base_name = os.path.basename(img_url)
print(base_name)

class_pred(classifier, img_url, base_name, IMAGE_SHAPE, imagenet_labels)