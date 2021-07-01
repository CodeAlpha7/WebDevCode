"""A video player class."""

from .video_library import VideoLibrary
import random
playlist_name_list = []



class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.prev = ""
        self.flag = 0



    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")




    def show_all_videos(self):
        print("Here's a list of all available videos:")
        all_videos = self._video_library.get_all_videos()
        sort_video_list = []
        for i in all_videos:
            sort_video_list.append([i.title, i.video_id, i.tags])
        
        sort_video_list.sort()

        for i in range(len(sort_video_list)):
            print(sort_video_list[i][0] + " (" + sort_video_list[i][1] + ") [", end="")
            for index in range(len(sort_video_list[i][2])):
                if index == len(sort_video_list[i][2]) - 1:
                    print(sort_video_list[i][2][index], end="")
                else:
                    print(sort_video_list[i][2][index], end=" ")
            print("]")


    def play_video(self, video_id):


        object = self._video_library.get_video(video_id)
        all_videos = self._video_library.get_all_videos()

        
        if object == None:
            print("Cannot play video: Video does not exist")
        
        
        else:
            if self.prev == "":
                print("Playing video: " + object.title)
                self.prev = object.title
                self.flag = 0
            
            else:
                # if self.flag == 0:
                print("Stopping video: " + self.prev)
                print("Playing video: " + object.title)
                self.prev = object.title
                self.flag = 0
                
                # else:
                #     if self.flag == 1:
                #         if self.prev == object.title:
                #             print("Playing video: " + object.title)
                #             self.prev = object.title
                #             self.flag = 0

                #         else:
                #             print("Stopping video: " + self.prev)
                #             print("Playing video: " + object.title)
                #             self.prev = object.title
                #             self.flag = 0    
                        



    def stop_video(self):

        if self.prev == "":
            print("Cannot stop video: No video is currently playing")
        
        else:
            print("Stopping video: " + self.prev)
            self.prev = ""
            self.flag = 0


    def play_random_video(self):


        all_videos = self._video_library.get_all_videos()
        random_video_list = []
        for i in all_videos:
            random_video_list.append(i.title)
        
        selected = random.choice(random_video_list)

        if self.prev == "":
            
            print("Playing video: " + selected)
            self.prev = selected
            self.flag = 0

        else:
            print("Stopping video: "+ self.prev)
            print("Playing video: " + selected)
            self.prev = selected
            self.flag = 0


    def pause_video(self):


        if self.prev == "":
            print("Cannot pause video: No video is currently playing")
        
        else:
            if self.flag == 0:
                print("Pausing video: " + self.prev)
                self.flag = 1
            
            else:
                if self.flag == 1:
                    print("Video already paused: " + self.prev)


    def continue_video(self):


        if self.flag == 1:
            print("Continuing video: "  + self.prev)
            self.flag = 0

        else:
            if self.prev == "":
                print("Cannot continue video: No video is currently playing")
            
            else:
                print("Cannot continue video: Video is not paused")



    def show_playing(self):
        all_videos = self._video_library.get_all_videos()
        sort_video_list = []
        for i in all_videos:
            sort_video_list.append([i.title, i.video_id, i.tags])

        if self.prev == "":
            print("No video is currently playing")
        
        else:
            if self.flag == 0:
                for i in all_videos:
                    if i.title == self.prev:
                        print("Currently playing: " + i.title + " (" + i.video_id + ") [", end="")
                        for index in range(len(i.tags)):
                            if index == len(i.tags) - 1:
                                print(i.tags[index], end="")
                            else:
                                print(i.tags[index], end=" ")
                        print("]")
            
            else:
                for i in all_videos:
                    if i.title == self.prev:
                        print("Currently playing: " + i.title + " (" + i.video_id + ") [", end="")
                        for index in range(len(i.tags)):
                            if index == len(i.tags) - 1:
                                print(i.tags[index], end="")
                            else:
                                print(i.tags[index], end=" ")
                        print("]", end="")
                print(" - PAUSED")



    def create_playlist(self, playlist_name):
        global playlist_name_list

        for i in playlist_name_list:
            if i == playlist_name:
                print("Cannot create playlist: A playlist with the same name already exits")

        playlist_name_list.append(playlist_name)
        print("Successfully created new playlist: " + playlist_name)

        
        

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as self.flagged.

        Args:
            video_id: The video_id to be self.flagged.
            self.flag_reason: Reason for self.flagging the video.
        """
        print("self.flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a self.flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
