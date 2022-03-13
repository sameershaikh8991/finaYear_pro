import numpy as np
import json
import torch
import torch.nn as nn
from  torch.utils.data import Dataset,DataLoader
from NeuralNetwork import *
from brain import *

with open('intent.json','r') as f:
	intents = json.load(f)


all_word = []
tags = []
xy = []

for intent in intents['intents']:
	tag = intent['tag']
	tags.append(tag)

	for pattern in intent['patterns']:
		# print(pattern)
		w = tokenize(pattern)
		all_word.extend(w)
		xy.append((w,tag))

ign_word =['.','?','/','!',',']

all_word = [stem(w) for w in all_word if w not in ign_word]
all_word = sorted(set(all_word))


x_train =[]
y_train = []

for (pattern_sentance,tag) in xy:
	bag = bag_of_words(pattern_sentance, all_word)
	x_train.append(bag)

	label = tags.index(tag)
	y_train.append(label)

x_train = np.array(x_train)
y_train = np.array(y_train)

num_expo = 1000
batch_size = 8
larning_rate =0.001
input_size = len(x_train[0])
hidden_size = 8
output_size =len(tags)

print("tranning model..")

class AiDataset(Dataset):
	def __init__(self):
		self.n_sample = len(x_train)
		self.x_data = x_train
		self.y_data = y_train

	def __getitem__(self,index):
		return self.x_data[index],self.y_data[index]


	def __len__(self):
		return self.n_sample

dataset = AiDataset()
trian_loader = DataLoader(dataset=dataset,batch_size=batch_size,shuffle=True,num_workers = 0)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

model  = NeuralNet(input_size, hidden_size,output_size).to(device=device)
cartoation = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(),lr=larning_rate)

for expo in range(num_expo):
	for (words, labels) in trian_loader:
		words = words.to(device)
		labels = labels.to(dtype=torch.long).to(device)
		outputs = model(words)
		loss = cartoation(outputs,labels)
		optimizer.zero_grad()
		loss.backward()
		optimizer.step()

	if(expo+1)% 100 ==0:
		print(f'expo [{expo+1}/{num_expo}],loss={loss.item():.4f}')


print(f'Final loss: {loss.item():.4f}')


data = {
	"model_state":model.state_dict(),
	"input_size":input_size,
	"hidden_size":hidden_size,
	"output_size":output_size,
	"all_words":all_word,
	"tags":tags
}

File = "traindata.pth"
torch.save(data,File)

print("tranning done")