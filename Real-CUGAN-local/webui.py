from infervideo import VideoRealWaifuUpScaler
import gradio as gr
import os
ModelPath = "weights_v3/"

def inference_video( input_video, model_name, input_scale ):
    from config import half, tile, scale, device, encode_params, p_sleep, decode_sleep, nt, n_gpu,cache_mode,alpha
    scale = input_scale
    model_path = ModelPath + model_name
    video_upscaler=VideoRealWaifuUpScaler(nt,n_gpu,scale,half,tile,cache_mode,alpha,p_sleep,decode_sleep,encode_params,model_path)
    
    #video path
    inp_path = os.path.abspath(input_video)
    opt_path = "process_video/input-2x.mp4"
    out_complete_path = os.path.abspath(opt_path)
    video_upscaler(input_video,opt_path)
    return out_complete_path

if __name__ == '__main__':
    
    video = gr.Video(label='Video')
    model_name = gr.Dropdown(os.listdir(ModelPath), value="up2x-latest-denoise2x.pth", label='CUGAN Model') #default="up2x-latest-denoise2x.pth"
    scale = gr.Dropdown([0, 1, 2, 3, 4], value=2, label='Scale (use some model scale)') #x2

    inputs = [ video, model_name, scale ]
    demo = gr.Interface(fn=inference_video, inputs=inputs, outputs="video")
    demo.launch(share=False)