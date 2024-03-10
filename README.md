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

![Screenshot 2024-03-10 134125](https://github.com/bibasrairockz/Hyper-Personalized-In-Game-Advertising/assets/130794180/af495c5a-5bc6-4d91-bb68-ce082c537730)


## Project snips  

![Screenshot 2024-03-10 135946](https://github.com/bibasrairockz/Hyper-Personalized-In-Game-Advertising/assets/130794180/7a5548fc-522f-4443-ac2e-17a461017e2b)



