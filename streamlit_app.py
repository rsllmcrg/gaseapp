import streamlit as st
import av
import numpy as np
import streamlit_webrtc as webrtc

def main():
    st.title("Take Photo Demo")
    
    webrtc_ctx = webrtc.StreamlitWebRTC(
        rtc_configuration={
            "iceServers": [{"urls": "stun:stun.l.google.com:19302"}],
        },
        media_stream_constraints={
            "video": True,
            "audio": False,
        },
        key="photo",
        height=480,
        mode=webrtc.WebRtcMode.SENDONLY,
    )

    if not webrtc_ctx.state.playing:
        st.warning("No video stream available.")
        return

    st.write("Press the button below to take a photo:")
    if st.button("Take Photo"):
        image = webrtc_ctx.image_filter(np.zeros((480, 640, 3), dtype=np.uint8))
        st.image(image)

if __name__ == "__main__":
    main()
