import java.util.ArrayList;
import java.util.List;

public class MeetingRoomScheduler {

    class Room {
        int roomID;
        List<int[]> timings = new ArrayList<>();

        Room(int[] timing, int roomID) {
            this.roomID = roomID;
            timings.add(timing);
        }

        public void addMeeting(int[] timings) {
            this.timings.add(timings);
        }

    }

    /**
     *
     * @param intervals
     * @return
     */
    public int minMeetingRooms(int[][] meetings) {

        for(int i=0; i<meetings.length-1; i++){
            for(int j=i+1; j<meetings.length; j++){
                if(meetings[i][0]>meetings[j][0]){
                    int[] tmp = meetings[i];

                    meetings[i]=meetings[j];
                    meetings[j] = tmp;
                }

            }
        }
        List<Room> roomList = new ArrayList<Room>();
        int roomIDCounter = 0;
        boolean roomAssigned = false;
        boolean overlap= false;
        for (int[] meeting : meetings) {
            if (roomIDCounter == 0) {
                roomIDCounter++;
                Room room = new Room(meeting, roomIDCounter);
                roomList.add(room);
            } else {
                // check Room, if there is no over lap add to Room
                for (Room room : roomList) {
                    roomAssigned= false;
                    overlap = false;
                    for (int[] time : room.timings) {
                        // Checking Overlap - - first No overlap

                        if (time[1] > meeting[0]) {
                            // room.addMeeting(time);
                            overlap = true;
                            break;
                        }
                    }
                    if(!overlap){
                        room.addMeeting(meeting);
                        roomAssigned=true;
                        break;
                    }

                }

                // If there is overlap find next room or create new room
                if(!roomAssigned){
                    roomIDCounter++;
                    Room room = new Room(meeting, roomIDCounter);
                    roomList.add(room);
                }
            }
        }
        System.out.println("Size --> "+ roomList.size());
        return roomList.size();
    }
}
