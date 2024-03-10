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
  
## Demo Videos:
### Input:  
https://github.com/bibasrairockz/Hyper-Personalized-In-Game-Advertising/assets/130794180/2a1357f4-ab1f-4908-91a3-8bac6b434cde  
  
### Final Output:  
https://github.com/bibasrairockz/Hyper-Personalized-In-Game-Advertising/assets/130794180/c31bc9ea-8b65-4510-ba1e-9d6c9808efa6


