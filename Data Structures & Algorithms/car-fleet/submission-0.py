class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        t_time=[]
        sorted_pos=sorted(zip(position,speed), reverse=True)
        for pos, speed in sorted_pos:
            t_cur=(target-pos)/speed
            if t_time and t_cur<=t_time[-1]:
                continue
            elif t_time and t_cur > t_time[-1] or not t_time:
                t_time.append(t_cur)
        return len(t_time)
        