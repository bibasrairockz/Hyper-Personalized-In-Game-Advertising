# Hyper-Personalized In-Game Advertising
This project automates the process of integrating advertisement images into detected billboard spaces within a series of video frames from video game footages. Utilizing a combination of object detection, segmentation, and image manipulation techniques, it identifies billboards in video frames, adjusts advertisements to fit these billboards' dimensions and perspective, and then seamlessly integrates them into the scene. This process creates a realistic insertion of advertisements into existing video footage, suitable for marketing and film production enhancements.

# Key Features

- **Automatic Billboard Detection**: Leverages GroundingDINO for accurate detection of billboard spaces within complex urban environments.
- **Precise Segmentation**: Utilizes SAM (Segment Anything Model) for generating detailed masks around the identified billboard areas, ensuring precise advertisement fitting.
- **Dynamic Advertisement Integration**: Adapts and integrates advertisement images into detected billboards using perspective transformation and alpha blending techniques.
- **Video Compilation**: Reassembles processed frames back into video format, maintaining the original footage's frame rate and resolution.
- **Custom Music/ Ads**: Depending on user's interests, generated music from text prompts can be added to the video game, similarly custom ads can be created from text prompts (from advertisers) and placed effectively within the game.


# Architecture 
![Pasted_image_20240310120119](https://github.com/bibasrairockz/Hyper-Personalized-In-Game-Advertising/assets/130794180/a3013527-4627-40d2-a8ff-b9f73363c997)  

# Acknowledgments
[GitHub - betogaona7/Grounded-Segment-Anything: Marrying Grounding DINO with Segment Anything & Stable Diffusion & BLIP & Whisper - Automatically Detect , Segment and Generate Anything with Image, Text, and Speech Inputs](https://github.com/betogaona7/Grounded-Segment-Anything?tab=readme-ov-file)

# TEAM
1. Deep Wilson ( deep.16wilson@gmail.com ) - Ideation, Computer Vision (Segmentation/ Contour detection/ Alpha blending)
2. Bibas Rai (bibasrai6@gmail.com) - Stable Diffusion (image generation), Backend/Frontend integration 
3. Deepak Singh (deepaksingh26113@gmail.com) - Music generation, Backend Intergration/front-end integration 
4. Kartik Gehlot (kartikgehlot963@gmail.com) - Model training/ integration
  
## Demo Videos  


https://github.com/bibasrairockz/Hyper-Personalized-In-Game-Advertising/assets/130794180/e0f79d82-ba7a-4d89-b30f-b6bd109f0d1f  


## GenAI (Image, Music)   
### Image:  
![Figure_16](https://github.com/bibasrairockz/Hyper-Personalized-In-Game-Advertising/assets/130794180/092e3a28-68fa-48cd-aa4d-15fd36a5b5cf)  
  
![Figure_15](https://github.com/bibasrairockz/Hyper-Personalized-In-Game-Advertising/assets/130794180/85708e67-7a5f-4d30-bac7-fef2d36c375e)  
  
![Figure_17](https://github.com/bibasrairockz/Hyper-Personalized-In-Game-Advertising/assets/130794180/70a1c548-0301-442d-933e-78a8fd42abfa)





