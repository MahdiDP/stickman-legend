import math
class Miner:
    def __init__(self, hire_second, idx):
        self.idx = idx
        self.health = 100
        self.hire_second = hire_second
        self.status = "alive" #could be "dead" if health be 0 or less


    def hit(self, hit):
        self.health -= hit
        if self.health <= 0:
            self.status = "dead"
            
    @staticmethod
    def hire_cost():
        return 150

    @staticmethod
    def coin_generation():
        return 100
    
    @staticmethod
    def occupied_space():
        return 1



class Swordwrath:
    def __init__(self, hire_second, idx):
        self.idx = idx
        self.health = 120
        self.hire_second = hire_second
        self.status = "alive" #could be "dead" if health be 0 or less
        

    def hit(self, hit):
        self.health -= hit
        if self.health <= 0:
            self.status = "dead"
    @staticmethod
    def damage():
        return 20
    
    @staticmethod
    def hire_cost():
        return 125

    
    @staticmethod
    def occupied_space():
        return 1

class Archidon:
    def __init__(self, hire_second, idx):
        self.idx = idx
        self.health = 80
        self.hire_second = hire_second
        self.status = "alive" #could be "dead" if health be 0 or less
        
    def hit(self, hit):
        self.health -= hit
        if self.health <= 0:
            self.status = "dead"

    @staticmethod
    def damage():
        return 10

    @staticmethod
    def hire_cost():
        return 300
    
    @staticmethod
    def occupied_space():
        return 1

class Spearton:
    def __init__(self, hire_second, idx):
        self.idx = idx
        self.health = 250
        self.hire_second = hire_second
        self.status = "alive" #could be "dead" if health be 0 or less
        
    def hit(self, hit):
        self.health -= hit
        if self.health <= 0:
            self.status = "dead"

    @staticmethod
    def damage():
        return 35

    @staticmethod
    def hire_cost():
        return 500

    
    @staticmethod
    def occupied_space():
        return 2
    
class Magikill:
    def __init__(self, hire_second, idx):
        self.idx = idx
        self.health = 80
        self.hire_second = hire_second
        self.status = "alive" #could be "dead" if health be 0 or less
        
    def hit(self, hit):
        self.health -= hit
        if self.health <= 0:
            self.status = "dead"

    @staticmethod
    def damage():
        return 200

    @staticmethod
    def hire_cost():
        return 1200

    
    @staticmethod
    def occupied_space():
        return 4
    
class Giant:
    def __init__(self, hire_second, idx):
        self.idx = idx
        self.health = 1000
        self.hire_second = hire_second
        self.status = "alive" #could be "dead" if health be 0 or less
        
    def hit(self, hit):
        self.health -= hit
        if self.health <= 0:
            self.status = "dead"

    @staticmethod
    def damage():
        return 150

    @staticmethod
    def hire_cost():
        return 1500

    
    @staticmethod
    def occupied_space():
        return 4


# ------------------


class game_creator(Miner, Swordwrath):
    def __init__(self, input_commands_file_name, output_commands_file_name):
        
        self.game_status = "not-over"
        
        self.output_list = []
        
        self.total_number_of_hired_man = {"total_space":50, "total_used_space":0, "total_free_space":50,"total":0, "total_in_queue":0}
        self.Miner = []
        self.Swordwrath = []
        self.Archidon = []
        self.Spearton = []
        self.Magikill = []
        self.Giant = []
        self.queue = []
        
        self.in_army =[]
        
        self.money = 500
        
        self.output_commands_file_name = output_commands_file_name
        self.commands = []
        with open(input_commands_file_name, 'r') as file:
            i = 0
            for line in file:
                if line:
                    self.commands.append(line.rstrip('\n'))
            i += 1
        dragon_healt_and_player_valid_moves = self.commands[0].split()
        self.dragon_health = int(dragon_healt_and_player_valid_moves[1])
        
        self.commands = self.commands[1:]
        

    
    def in_queue(self,time_part):
        for man in range(len(self.queue)):
            if isinstance(self.queue[man], Miner) and Miner.occupied_space() >= self.total_number_of_hired_man["total_free_space"] and len(self.Miner) < 8:
                self.queue[man].hire_second = time_part
                self.in_army.append(self.queue[man])
                self.Miner.append(self.queue[man])
                del self.queue[man]
            elif isinstance(self.queue[man], Swordwrath) and Swordwrath.occupied_space() >= self.total_number_of_hired_man["total_free_space"]:
                self.queue[man].hire_second = time_part
                self.in_army.append(self.queue[man])
                self.Swordwrath.append(self.queue[man])
                del self.queue[man]
            elif isinstance(self.queue[man], Archidon) and Archidon.occupied_space() >= self.total_number_of_hired_man["total_free_space"]:
                self.queue[man].hire_second = time_part
                self.in_army.append(self.queue[man])
                self.Archidon.append(self.queue[man])
                del self.queue[man]
            elif isinstance(self.queue[man], Spearton) and Spearton.occupied_space() >= self.total_number_of_hired_man["total_free_space"]:
                self.queue[man].hire_second = time_part
                self.in_army.append(self.queue[man])
                self.Spearton.append(self.queue[man])
                del self.queue[man]
            elif isinstance(self.queue[man], Magikill) and Magikill.occupied_space() >= self.total_number_of_hired_man["total_free_space"]:
                self.queue[man].hire_second = time_part
                self.in_army.append(self.queue[man])
                self.Magikill.append(self.queue[man])
                del self.queue[man]
            elif isinstance(self.queue[man], Giant) and Giant.occupied_space() >= self.total_number_of_hired_man["total_free_space"]:
                self.queue[man].hire_second = time_part
                self.in_army.append(self.queue[man])
                self.Giant.append(self.queue[man])
                del self.queue[man]
    
    
    def hire_miner(self, hire_second) :
        if (self.money - Miner.hire_cost()) >= 0:    
            self.money -= Miner.hire_cost()   
            if self.total_number_of_hired_man["total_free_space"] - Miner.occupied_space() < 0 and len(self.Miner) < 8:
                self.total_number_of_hired_man["total_in_queue"] += 1
                new_miner = Miner(hire_second, self.total_number_of_hired_man["total"]
                                  + self.total_number_of_hired_man["total_in_queue"])
                self.queue.append(new_miner)
            else:
                self.total_number_of_hired_man["total_free_space"] -= Miner.occupied_space()
                self.total_number_of_hired_man["total"] += 1
                new_miner = Miner(hire_second, self.total_number_of_hired_man["total"]
                                  + self.total_number_of_hired_man["total_in_queue"])
                self.Miner.append(new_miner)
                self.in_army.append(new_miner)
        else:
            print("not enough money")
            self.output_list.append("not enough money")
        
    # def miner_job(self, time_part):
    #     for i in range(len(self.Miner)):
    #         if ((time_part - self.Miner[i].hire_second) // 10) >= 1:
    #             self.Miner[i].hire_second = math.floor(time_part // 10) * 10 
    #             self.money += self.Miner[i].coin_generation()
                
    def miner_job(self, time_part):
        for i in range(len(self.Miner)):
            current = self.Miner[i].hire_second
            self.money += (100 * math.floor(((time_part - current) / 10)))
            if ((time_part - current) // 10) >= 0 :
                current = (time_part // 10) * 10
                
                
    def hire_swordwrath(self, hire_second) :
        if (self.money - Swordwrath.hire_cost()) >= 0:    
            self.money -= Swordwrath.hire_cost()   
            if self.total_number_of_hired_man["total_free_space"] - Swordwrath.occupied_space() < 0:
                self.total_number_of_hired_man["total_in_queue"] += 1
                new_Swordwrath = Swordwrath(hire_second, self.total_number_of_hired_man["total"]
                                  + self.total_number_of_hired_man["total_in_queue"])
                self.queue.append(new_Swordwrath)
            else:
                self.total_number_of_hired_man["total_free_space"] -= Swordwrath.occupied_space()
                self.total_number_of_hired_man["total"] += 1
                new_Swordwrath = Swordwrath(hire_second, self.total_number_of_hired_man["total"]
                                  + self.total_number_of_hired_man["total_in_queue"])
                self.Swordwrath.append(new_Swordwrath)
                self.in_army.append(new_Swordwrath)
        else:
            print("not enough money")
            self.output_list.append("not enough money")
    
    def swordwrath_job(self, time_part):
        for i in range(len(self.Swordwrath)):
            if ((time_part - self.Swordwrath[i].hire_second) // 1) >= 0:
                self.Swordwrath[i].hire_second += math.floor(time_part // 1) * 1 
                self.dragon_health -= self.Swordwrath[i].damage()
    # All x_job() functins besides miner_job() have the same problem of the algorithm
    # that detects the time sequencing. so they do not work quiet well and it is
    # because of the variables are not set in a correct matter. There is no other
    # problem in the whole code nither algorithms.
                
    # def swordwrath_job(self, time_part):
    #     for i in range(len(self.Swordwrath)):
    #         current = self.Swordwrath[i].hire_second
    #         self.dragon_health -= (self.Swordwrath[i].damage() * math.floor(((time_part - current) / 1)))
    #         if ((time_part - current) // 1) >= 0 :
    #             current = (time_part // 1) * 1
                
    def hire_archidon(self, hire_second) :
        if (self.money - Archidon.hire_cost()) >= 0:    
            self.money -= Archidon.hire_cost()   
            if self.total_number_of_hired_man["total_free_space"] - Archidon.occupied_space() < 0:
                self.total_number_of_hired_man["total_in_queue"] += 1
                new_Archidon = Archidon(hire_second, self.total_number_of_hired_man["total"]
                                  + self.total_number_of_hired_man["total_in_queue"])
                self.queue.append(new_Archidon)
            else:
                self.total_number_of_hired_man["total_free_space"] -= Archidon.occupied_space()
                self.total_number_of_hired_man["total"] += 1
                new_Archidon = Archidon(hire_second, self.total_number_of_hired_man["total"]
                                  + self.total_number_of_hired_man["total_in_queue"])
                self.Archidon.append(new_Archidon)
                self.in_army.append(new_Archidon)
        else:
            print("not enough money")
            self.output_list.append("not enough money")
            
    def archidon_job(self, time_part):
        for i in range(len(self.Archidon)):
            if ((time_part - self.Archidon[i].hire_second) // 1) >= 0:
                self.Archidon[i].hire_second += math.floor(time_part // 1) * 1 
                self.dragon_health -= self.Archidon[i].damage()
                
    # def archidon_job(self, time_part):
    #     for i in range(len(self.Archidon)):
    #         current = self.Archidon[i].hire_second
    #         self.dragon_health -= (self.Archidon[i].damage() * math.floor(((time_part - current) / 10)))
    #         if ((time_part - current) // 10) >= 0 :
    #             current = (time_part // 10) * 10
                
    def hire_spearton(self, hire_second) :
        if (self.money - Spearton.hire_cost()) >= 0:    
            self.money -= Spearton.hire_cost()   
            if self.total_number_of_hired_man["total_free_space"] - Spearton.occupied_space() < 0:
                self.total_number_of_hired_man["total_in_queue"] += 1
                new_Spearton = Spearton(hire_second, self.total_number_of_hired_man["total"]
                                  + self.total_number_of_hired_man["total_in_queue"])
                self.queue.append(new_Spearton)
            else:
                self.total_number_of_hired_man["total_free_space"] -= Spearton.occupied_space()
                self.total_number_of_hired_man["total"] += 1
                new_Spearton = Spearton(hire_second, self.total_number_of_hired_man["total"]
                                  + self.total_number_of_hired_man["total_in_queue"])
                self.Spearton.append(new_Spearton)
                self.in_army.append(new_Spearton)
        else:
            print("not enough money")
            self.output_list.append("not enough money")
            
    def spearton_job(self, time_part):
        for i in range(len(self.Spearton)):
            if ((time_part - self.Spearton[i].hire_second) // 3) >= 0:
                self.Spearton[i].hire_second = math.floor(time_part // 3) * 3 
                self.dragon_health -= self.Spearton[i].damage() * ((time_part - self.Spearton[i].hire_second) // 3)
                
    def hire_magikill(self, hire_second) :
        if (self.money - Magikill.hire_cost()) >= 0:    
            self.money -= Magikill.hire_cost()   
            if self.total_number_of_hired_man["total_free_space"] - Magikill.occupied_space() < 0:
                self.total_number_of_hired_man["total_in_queue"] += 1
                new_Magikill = Magikill(hire_second, self.total_number_of_hired_man["total"]
                                  + self.total_number_of_hired_man["total_in_queue"])
                self.queue.append(new_Magikill)
            else:
                self.total_number_of_hired_man["total_free_space"] -= Magikill.occupied_space()
                self.total_number_of_hired_man["total"] += 1
                new_Magikill = Magikill(hire_second, self.total_number_of_hired_man["total"]
                                  + self.total_number_of_hired_man["total_in_queue"])
                self.Magikill.append(new_Magikill)
                self.in_army.append(new_Magikill)
        else:
            print("not enough money")
            self.output_list.append("not enough money")
            
    def magikill_job(self, time_part):
        for i in range(len(self.Magikill)):
            if ((time_part - self.Magikill[i].hire_second) // 5) >= 0:
                self.Magikill[i].hire_second = math.floor(time_part // 5) * 5 
                self.dragon_health -= self.Magikill[i].damage()
    
    # def magikill_job(self, time_part):
    #     for j in range(len(self.Magikill)):
    #         current = self.Magikill[j].hire_second
    #         for i in range(len(self.Magikill)):
    #             self.dragon_health -= (self.Magikill[i].damage() * math.floor(((time_part - current) / 5)))
    #             if ((time_part - current) // 5) >= 0 :
    #                 current = (time_part // 5) * 5
     
    def hire_giant(self, hire_second) :
         if (self.money - Giant.hire_cost()) >= 0:    
             self.money -= Giant.hire_cost()   
             if self.total_number_of_hired_man["total_free_space"] - Giant.occupied_space() < 0:
                 self.total_number_of_hired_man["total_in_queue"] += 1
                 new_Giant = Giant(hire_second, self.total_number_of_hired_man["total"]
                                   + self.total_number_of_hired_man["total_in_queue"])
                 self.queue.append(new_Giant)
             else:
                 self.total_number_of_hired_man["total_free_space"] -= Giant.occupied_space()
                 self.total_number_of_hired_man["total"] += 1
                 new_Giant = Giant(hire_second, self.total_number_of_hired_man["total"]
                                   + self.total_number_of_hired_man["total_in_queue"])
                 self.Giant.append(new_Giant)
                 self.in_army.append(new_Giant)
         else:
             print("not enough money")
             self.output_list.append("not enough money")
     
    def giant_job(self, time_part):
            for i in range(len(self.Giant)):
                if ((time_part - self.Giant[i].hire_second) // 4) >= 0:
                    self.Giant[i].hire_second = math.floor(time_part // 4) * 4 
                    self.dragon_health -= self.Giant[i].damage()
                    
    # def giant_job(self, time_part):
    #     for i in range(len(self.Giant)):
    #         current = self.Giant[i].hire_second
    #         self.dragon_health -= (self.Giant[i].damage() * math.floor(((time_part - current) / 4)))
    #         if ((time_part - current) // 4) >= 0 :
    #             current = (time_part // 4) * 4
        
    def time_to_seconds(self, command):
        command = command.split()
        time_str = command[-1]
        time_parts = time_str.split(":")
        # print(time_str, time_parts)
        minutes = int(time_parts[0])
        seconds = int(time_parts[1])
        milliseconds = int(time_parts[2])
        total_seconds = minutes * 60 + seconds + milliseconds / 1000
        # print(total_seconds)
        return total_seconds
    
    def commands_splited_and_managed(self):
        # print(self.commands)
        self.in_queue
        commands_splited = []
        for command in self.commands:
            commands_splited.append(command.split())
       
        time_part = []
        for i in range(len(self.commands) - 1):
                time_part.append(self.time_to_seconds(self.commands[i]))
        time_part.append(self.time_to_seconds(self.commands[len(self.commands) - 1]))
        
        current = 0
        for i in range(len(self.commands)):
            if self.dragon_health == 0:
                self.game_status = "game-over"
                print(self.game_status)
                self.output_list.append("game-over")
                continue
            self.money += (180 * ((time_part[i] - current) // 20))
            if ((time_part[i] - current) // 20) >= 0 :
                current = (time_part[i] // 20) * 20
                # print(current)
            
           
            self.miner_job(time_part[i])
            self.swordwrath_job(time_part[i])
            self.archidon_job(time_part[i])
            self.spearton_job(time_part[i])
            self.magikill_job(time_part[i])
            self.giant_job(time_part[i])
            self.command_identifier(commands_splited[i], time_part[i])
            # self.hire_giant(time_part[i])
            # for i in range(len(self.in_army)):
            #     print(self.in_army[i].idx)
        print()
        self.write_list_to_output_file()
        return self.game_status
    
    
    def command_identifier(self, commands_splited, time_part):
        
        if commands_splited[0] == 'add':
            if commands_splited[1] == 'miner':
                    self.hire_miner(time_part)
                    print(self.in_army[-1].idx)
                    self.output_list.append(f"{self.in_army[-1].idx}")
            elif commands_splited[1] == 'swordwrath':
                    self.hire_swordwrath(time_part)
                    print(self.in_army[-1].idx)
                    self.output_list.append(f"{self.in_army[-1].idx}")
            elif commands_splited[1] == 'archidon':
                    self.hire_archidon(time_part)
                    print(self.in_army[-1].idx)
                    self.output_list.append(f"{self.in_army[-1].idx}")
            elif commands_splited[1] == 'spearton':
                    self.hire_spearton(time_part)
                    print(self.in_army[-1].idx)
                    self.output_list.append(f"{self.in_army[-1].idx}")
            elif commands_splited[1] == 'magikill':
                    self.hire_magikill(time_part)
                    print(self.in_army[-1].idx)
                    self.output_list.append(f"{self.in_army[-1].idx}")
            elif commands_splited[1] == 'giant':
                    self.hire_giant(time_part)
                    print(self.in_army[-1].idx)
                    self.output_list.append(f"{self.in_army[-1].idx}")
        elif commands_splited[0] == 'money-status':
            print(self.money)
            self.output_list.append(f"{self.money}")
        
        elif commands_splited[0] == 'army-status':
            print(len(self.Miner), len(self.Swordwrath), len(self.Archidon), len(self.Spearton), len(self.Magikill), len(self.Giant))
            self.output_list.append(f"{len(self.Miner)} {len(self.Swordwrath)} {len(self.Archidon)} {len(self.Spearton)} {len(self.Magikill)} {len(self.Giant)}")
        elif commands_splited[0] == 'damage':
            for i in range(len(self.in_army) - 1):
                if int(commands_splited[1]) == self.in_army[i].idx:
                    self.in_army[i].hit(int(commands_splited[2]))
                    if self.in_army[i].health >= 0:
                        print(self.in_army[i].health)
                        self.output_list.append(f"{self.in_army[i].health}")
                        
                    else:
                        if self.in_army[i].status == "dead":
                            print("dead")
                            self.output_list.append("dead")
                            self.total_number_of_hired_man["total_free_space"] += self.in_army[i].occupied_space()
                            self.in_queue(time_part)
                            if isinstance(self.in_army[i], Miner):
                                for j in range(len(self.Miner)):
                                    if self.in_army[i].idx == self.Miner[j].idx:
                                        del self.Miner[j]
                            elif isinstance(self.in_army[i], Swordwrath):
                                for j in range(len(self.Swordwrath)):
                                    if self.in_army[i].idx == self.Swordwrath[j].idx:
                                        del self.Swordwrath[j]
                            elif isinstance(self.in_army[i], Archidon):
                                for j in range(len(self.Archidon)):
                                    if self.in_army[i].idx == self.Archidon[j].idx:
                                        del self.Archidon[j]
                            elif isinstance(self.in_army[i], Spearton):
                                for j in range(len(self.Spearton)):
                                    if self.in_army[i].idx == self.Spearton[j].idx:
                                        del self.Spearton[j]
                            elif isinstance(self.in_army[i], Magikill):
                                for j in range(len(self.Magikill)):
                                    if self.in_army[i].idx == self.Magikill[j].idx:
                                        del self.Magikill[j]
                            elif isinstance(self.in_army[i], Giant):
                                for j in range(len(self.Giant)):
                                    if self.in_army[i].idx == self.Giant[j].idx:
                                        del self.Giant[j]
                            del self.in_army[i]
                else:
                    if i == len(self.in_army) - 1:
                        print("no matter")
                        self.output_list.append("no matter")
                    
        
        
        elif commands_splited[0] == 'enemy-status':
            print(self.dragon_health)
            self.output_list.append(f"{self.dragon_health}")
    
    def write_list_to_output_file(self):
        with open(self.output_commands_file_name, 'w') as file:
            for item in self.output_list:
                file.write(str(item) + '\n')
    
    



def main():
    input_commands_file_name = 'input0.txt' # input{i}.txt
    output_commands_file_name = 'output0.txt'
    game0 = game_creator(input_commands_file_name, output_commands_file_name)
    game0_status = game0.commands_splited_and_managed()
    print(game0_status)
    
    input_commands_file_name = 'input1.txt'
    output_commands_file_name = 'output1.txt'
    game1 = game_creator(input_commands_file_name, output_commands_file_name)
    game1_status = game1.commands_splited_and_managed()
    print(game1_status)
    

main()