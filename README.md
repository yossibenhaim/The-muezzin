# The-muezzin

Audio file collection software - transcription and data analysis
## 🔧 Technologies

- Language: python
- Environment: Pycram
- Project Type: Console Application

## 📁 Project Structure

```
The-muezzin/
│
├── consumer 
│   ├── kafka_consumer
│   │   └── sub-consumer.py
│   ├── utils
│   │   └── utils_consumer.py
│   ├── write_to_elasticsearch
│   │   └── write_to_elasticsearch.py
│   ├── write_to_mongo
│   │   └── write_to_mongoDB.py
│   ├── logger.py
│   ├── manager_consumer.py
├── information_analysis 
│   ├── decoding_words
│   │   └── decoding_words.py
│   ├── information_analysis
│   │   └── analysis.py
│   ├── kafka_analysis
│   │   └── sub-analysis.py
│   ├── utils
│   │   └── utils_analysis.py
│   ├── write_to_elasticsearch
│   │   └── write_to_elasticsearch.py
│   ├── manager_consumer.py
│   └── logger.py
├── producer 
│   ├── kafka_producer
│   │   └── kafka_producer.py
│   ├── reading_files
│   │   └── reading_files.py
│   ├── manager_producer.py
│   ├── utils_producer.py
│   └── logger.py
├── speach_to_text 
│   ├── kafka_stt
│   │   ├── producer_to_analysis.py
│   │   └── sub-stt.py
│   ├── speach_to_text
│   │   └── speach_to_text.py
│   ├── utils
│   │   └── utils_stt.py
│   ├── write_to_elasticsearch
│   │   └── write_to_elasticsearch.py
│   ├── manager_stt.py
│   └── logger.py
├── .env     
├── commend.bat    
├── .gitignore   
├── README.md   
└── requirements.txt             
```

## 🧠 Main features

- **producer**: Opens the audio recordings and creates metadata, sends them to Kafka to consumer and speach_to_text.
- **consumer**: Listener to Kafka receives documents, generates a unique id for them, and sends the metadata to Elastic for storage, and the file itself to MongoDB in byte encoding.
- **speach_to_text**: Listener to Kafka receives a route to files and performs transcription on them, sends the transcription to storage by id in Elastic, and sends the transcription to Kafka for information_analysis to extract information from the information.
- **information-analysis**: Listener to Kafka receives the files and performs an information search on them. Sends all the information for updating by the unique id in Elastic.

## ▶️ How to Run

1. Clone or download the repository.
2. Open the project in Visual Studio or Rider.
3. Set the `Program.cs` (if available) to call `IDF.print()` after initializing the system.
4. Build and run the solution.

```csharp
// Example initialization (you may add to Program.cs or Main):
var tolls = new tolls(); // Make sure to initialize with weapons
var terrorists = new ListAllTerrorist();
terrorists.Terrorist_creator();
var idf = new IDF(tolls, terrorists);
idf.print();
```
# Versions
Tuna has 2 versions:

local run and Docker deployment.

Please select the desired version.

## 📜 Explanations of decisions
#### In calculating the risk score
In the analysis, I check the risk level of the text. 
I calculate how many dangerous words there are, 
take the number and calculate what percentage of the text is dangerous.
---
#### Calculating the level of danger
If more than 0.5 the text is classified as high risk.
If more than 0.1 the text is classified as medium.
Less than that is considered none
---
#### Checking whether there is a risk
I perform a calculation based on the score. 
If it is above 0.1, it is considered dangerous and the software will return true.

## The emojis and the base of the readme file were taken from a previous project built with AI
# All content written solely by
### yossi ben haim
