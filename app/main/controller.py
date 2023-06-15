from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from ..models import Video
from flask import flash
import os


class MainController:
    """Manages the business logic of the main blueprint."""

    DEVELOPER_KEY = os.environ.get('YOUTUBE_API_KEY')
    YOUTUBE_API_SERVICE_NAME = 'youtube'
    YOUTUBE_API_VERSION = 'v3'

    def __init__(self):
        self.youtube_build = build(
            self.YOUTUBE_API_SERVICE_NAME, self.YOUTUBE_API_VERSION,
            developerKey=self.DEVELOPER_KEY)
        self.videos = []
        self.default_kw = 'Mental Energy'

    def fetch_yt_videos(self, search_kw):
        """Fetch youtube videos related to the search keyword."""
        try:
            # fetch the items matching the query keyword passed.
            search_res = self.youtube_build.search().list(
                q=search_kw, part='id,snippet'
            ).execute()

            for search_item in search_res.get('items', []):
                if search_item['id']['kind'] == 'youtube#video':
                    video_data = {}

                    # extract thumbnail url
                    thumbnail = search_item.get('snippet', {}).get(
                        'thumbnails', {}).get('default')
                    if thumbnail:
                        video_data['thumbnail'] = thumbnail['url']
                    
                    # extract video url
                    video_url = search_item.get('id', {}).get('videoId')
                    if video_url:
                        video_data['url'] = 'https://www.youtube.com/embed/' + video_url
                    
                    # extract video title
                    video_title = search_item.get('snippet', {}).get('title')
                    if video_title:
                        video_data['title'] = video_title
                    
                    # extract video description
                    video_description = search_item.get('snippet', {}).get(
                        'description')
                    if video_description:
                        video_data['desc'] = video_description
                    # add video to the list
                    self.videos.append(video_data)
        except Exception as e:
            message = str(e)

            if type(e) is HttpError:
                message = e.reason

            flash(message, 'error')
    
    def get_videos(self):
        """Extract all videos from the database."""
        self.videos = Video.get_all()
        return self.videos
    
    def save_videos(self):
        """Save all videos to the database if they don't already exist."""
        for video_data in self.videos:
            try:
                if not Video.get_one_by(url=video_data['url']):
                    new_video = Video(**video_data)

                    # save new video
                    new_video.save()
                    print(f'Saved video: {new_video.title}')
            except HttpError as e:
                print(f'Could not save video: {str(e)}.')
