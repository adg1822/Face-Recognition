def getclass(emmbeding):
  present, dist, name1 =  who_are_you(emmbeding)
  # prediction for the face
  samples = expand_dims(emmbeding, axis=0)
  #samples= in_encoder.transform(samples)
  yhat_class = Modelsvm.predict(samples)
  yhat_prob = Modelsvm.predict_proba(samples)

  # get name
  class_index = yhat_class[0]
  class_probability = yhat_prob[0,class_index] * 100
  name2 = out_encoder.inverse_transform(yhat_class)
  name2 = name2[0]

  if present and class_probability >=99.9999: 
    return name2
  elif present and class_probability <99:
    return 'unknown'
  elif present==False and name1==name2 and class_probability>=99.999:
   return name2
  else:
    return 'unknown'
