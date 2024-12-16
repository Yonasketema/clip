export const createAgentWork = async () => {
  const res = await fetch(new Request(`http://localhost:3000/api/`), {
    method: "POST",
  });
  const data = await res.json();
  return data;
};

export const getAgentsData = async (id: string) => {
  const res = await fetch(new Request(`http://localhost:3000/api/${id}`));
  const data = await res.json();
  return data.data;
};

const uploadVideo = async (title: string) => {
  const url = "https://open.tiktokapis.com/v2/post/publish/video/init/";
  const accessToken = "act.example12345Example12345Example";

  const headers = {
    Authorization: `Bearer ${accessToken}`,
    "Content-Type": "application/json; charset=UTF-8",
  };

  const data = {
    post_info: {
      title,
      privacy_level: "MUTUAL_FOLLOW_FRIENDS",
      disable_duet: false,
      disable_comment: true,
      disable_stitch: false,
      video_cover_timestamp_ms: 1000,
    },
    source_info: {
      source: "PULL_FROM_URL",
      video_url: "https://example.verified.domain.com/example_video.mp4",
    },
  };

  try {
    const response = await fetch(url, {
      method: "POST",
      headers: headers,
      body: JSON.stringify(data),
    });

    if (!response.ok) {
      throw new Error("Failed to upload video");
    }

    const responseData = await response.json();
    console.log("Video uploaded successfully:", responseData);
  } catch (error) {
    console.error("Error uploading video:", error);
  }
};
