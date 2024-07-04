
class Data:
    def __init__(self, grid_size, speed_factor):
        self.grid_size = grid_size

        self.speed_factor = speed_factor
        self.speed_of_movements_line2 = 1.5/4 + self.speed_factor
        self.speed_of_movements_line3 = 1.8/4 + self.speed_factor
        self.speed_of_movements_line4 = 1.1/4 + self.speed_factor
        self.speed_of_movements_line5 = 2.2/4 + self.speed_factor

        self.speed_of_movements_line8 = 1.5/4 + self.speed_factor
        self.speed_of_movements_line9 = 1.8/4 + self.speed_factor
        self.speed_of_movements_line10 = 1.1/4 + self.speed_factor
        self.speed_of_movements_line11 = 2.2/4 + self.speed_factor

        y_position_line2 = grid_size
        y_position_line3 = grid_size * 2
        y_position_line4 = grid_size * 3
        y_position_line5 = grid_size * 4

        y_position_line8 = grid_size * 7
        y_position_line9 = grid_size * 8
        y_position_line10 = grid_size * 9
        y_position_line11 = grid_size * 10

        self.movements_data_constructor = [
            [
                ("imagesMovements/TurtleWalk288x48px.png", self.speed_of_movements_line2, -grid_size,
                 y_position_line2, 288 / 6, 48, 6, 1, True, False),
                ("imagesMovements/TurtleWalk288x48px.png", self.speed_of_movements_line2,
                 grid_size * 10, y_position_line2, 288 / 6, 48, 6, 1, True, False),
                ("imagesMovements/TurtleWalk288x48px.png", self.speed_of_movements_line2,
                 grid_size * 18, y_position_line2, 288 / 6, 48, 6, 1, True, False),
                ("imagesMovements/eel_Attack.png", self.speed_of_movements_line2,
                 grid_size * 7, y_position_line2, 288 / 6, 48, 6, 1, True, True),
                ("imagesMovements/tree.png", self.speed_of_movements_line2, grid_size * 3,
                 y_position_line2, 128, 128, 1, 1, True, False),
                ("imagesMovements/tree.png", self.speed_of_movements_line2, grid_size * 5,
                 y_position_line2, 128, 128, 1, 1, True, False),
                ("imagesMovements/tree.png", self.speed_of_movements_line2, grid_size * 14,
                 y_position_line2, 128, 128, 1, 1, True, False)
            ],
            [
                ("imagesMovements/TurtleWalk288x48px.png", self.speed_of_movements_line3, grid_size * 6,
                 y_position_line3, 288 / 6, 48, 6, 1, False, False),
                ("imagesMovements/TurtleWalk288x48px.png", self.speed_of_movements_line3, grid_size * 15,
                 y_position_line3, 288 / 6, 48, 6, 1, False, False),
                ("imagesMovements/eel_Attack.png", self.speed_of_movements_line3, grid_size * 9,
                 y_position_line3, 288 / 6, 48, 6, 1, False, True),
                ("imagesMovements/eel_Attack.png", self.speed_of_movements_line3, grid_size * 17,
                 y_position_line3, 288 / 6, 48, 6, 1, False, True),
                ("imagesMovements/eel_Attack.png", self.speed_of_movements_line3, grid_size * 4,
                 y_position_line3, 288 / 6, 48, 6, 1, False, True),
                ("imagesMovements/tree.png", self.speed_of_movements_line3, grid_size * 2,
                 y_position_line3, 128, 128, 1, 1, False, False),
                ("imagesMovements/tree.png", self.speed_of_movements_line3, grid_size * 19,
                 y_position_line3, 128, 128, 1, 1, False, False)
            ],
            [
                ("imagesMovements/TurtleWalk288x48px.png", self.speed_of_movements_line4,
                 grid_size * 12, y_position_line4, 288 / 6, 48, 6, 1, True, False),
                ("imagesMovements/TurtleWalk288x48px.png", self.speed_of_movements_line4,
                 grid_size * 20, y_position_line4, 288 / 6, 48, 6, 1, True, False),
                ("imagesMovements/eel_Attack.png", self.speed_of_movements_line4, grid_size * 2,
                 y_position_line4, 288 / 6, 48, 6, 1, True, True),
                ("imagesMovements/eel_Attack.png", self.speed_of_movements_line4, grid_size * 4,
                 y_position_line4, 288 / 6, 48, 6, 1, True, True),
                ("imagesMovements/tree.png", self.speed_of_movements_line4, grid_size * 6,
                 y_position_line4, 128, 128, 1, 1, True, False),
                ("imagesMovements/tree.png", self.speed_of_movements_line4, grid_size * 8,
                 y_position_line4, 128, 128, 1, 1, True, False),
                ("imagesMovements/tree.png", self.speed_of_movements_line4, grid_size * 10,
                 y_position_line4, 128, 128, 1, 1, True, False),
                ("imagesMovements/tree.png", self.speed_of_movements_line4, grid_size * 15,
                 y_position_line4, 128, 128, 1, 1, True, False)
            ],
            [
                ("imagesMovements/TurtleWalk288x48px.png", self.speed_of_movements_line5,
                 grid_size, y_position_line5, 288 / 6, 48, 6, 1, False, False),
                ("imagesMovements/TurtleWalk288x48px.png", self.speed_of_movements_line5,
                 grid_size * 11, y_position_line5, 288 / 6, 48, 6, 1, False, False),
                ("imagesMovements/eel_Attack.png", self.speed_of_movements_line5, grid_size * 8,
                 y_position_line5, 288 / 6, 48, 6, 1, False, True),
                ("imagesMovements/eel_Attack.png", self.speed_of_movements_line5, grid_size * 20,
                 y_position_line5, 288 / 6, 48, 6, 1, False, True),
                ("imagesMovements/tree.png", self.speed_of_movements_line5, grid_size * 5,
                 y_position_line5, 128, 128, 1, 1, False, False),
                ("imagesMovements/tree.png", self.speed_of_movements_line5, grid_size * 3,
                 y_position_line5, 128, 128, 1, 1, False, False),
                ("imagesMovements/tree.png", self.speed_of_movements_line5, grid_size * 14,
                 y_position_line5, 128, 128, 1, 1, False, False),
                ("imagesMovements/tree.png", self.speed_of_movements_line5, grid_size * 18,
                 y_position_line5, 128, 128, 1, 1, False, False)
            ],
            [
                ("imagesMovements/Car1_Ride1536x192.png", self.speed_of_movements_line8, grid_size * 10,
                 y_position_line8 - 12, 1536 / 8, 192, 8, 1, False, False),
                ("imagesMovements/Car1_Ride1536x192.png", self.speed_of_movements_line8, grid_size * 15,
                 y_position_line8 - 12, 1536 / 8, 192, 8, 1, False, False),
                ("imagesMovements/Car2_Ride2048x256.png", self.speed_of_movements_line8, grid_size * 2,
                 y_position_line8 - 12, 2048 / 8, 256, 8, 1, False, False),
                ("imagesMovements/Car2_Ride2048x256.png", self.speed_of_movements_line8, grid_size * 5,
                 y_position_line8 - 12, 2048 / 8, 256, 8, 1, False, False),
                ("imagesMovements/Car2_Ride2048x256.png", self.speed_of_movements_line8, grid_size * 18,
                 y_position_line8 - 12, 2048 / 8, 256, 8, 1, False, False),
                ("imagesMovements/Car3_Ride1536x192.png", self.speed_of_movements_line8, grid_size * 7,
                 y_position_line8 - 12, 1536 / 8, 192, 8, 1, False, False),
                ("imagesMovements/Car3_Ride1536x192.png", self.speed_of_movements_line8, grid_size * 13,
                 y_position_line8 - 12, 1536 / 8, 192, 8, 1, False, False)
            ],
            [
                ("imagesMovements/Car1_Ride1536x192.png", self.speed_of_movements_line9, grid_size,
                 y_position_line9 - 12, 1536 / 8, 192, 8, 1, True, False),
                ("imagesMovements/Car2_Ride2048x256.png", self.speed_of_movements_line9, grid_size * 4,
                 y_position_line9 - 12, 2048 / 8, 256, 8, 1, True, False),
                ("imagesMovements/Car2_Ride2048x256.png", self.speed_of_movements_line9, grid_size * 14,
                 y_position_line9 - 12, 2048 / 8, 256, 8, 1, True, False),
                ("imagesMovements/Car3_Ride1536x192.png", self.speed_of_movements_line9, grid_size * 9,
                 y_position_line9 - 12, 1536 / 8, 192, 8, 1, True, False),
                ("imagesMovements/Car3_Ride1536x192.png", self.speed_of_movements_line9, grid_size * 11,
                 y_position_line9 - 12, 1536 / 8, 192, 8, 1, True, False)
            ],
            [
                ("imagesMovements/Car1_Ride1536x192.png", self.speed_of_movements_line10, grid_size * 13,
                 y_position_line10 - 12, 1536 / 8, 192, 8, 1, False, False),
                ("imagesMovements/Car2_Ride2048x256.png", self.speed_of_movements_line10, grid_size * 20,
                 y_position_line10 - 12, 2048 / 8, 256, 8, 1, False, False),
                ("imagesMovements/Car3_Ride1536x192.png", self.speed_of_movements_line10, grid_size * 3,
                 y_position_line10 - 12, 1536 / 8, 192, 8, 1, False, False),
                ("imagesMovements/Car3_Ride1536x192.png", self.speed_of_movements_line10, grid_size * 17,
                 y_position_line10 - 12, 1536 / 8, 192, 8, 1, False, False)
            ],
            [
                ("imagesMovements/Car1_Ride1536x192.png", self.speed_of_movements_line11, grid_size * 7,
                 y_position_line11 - 12, 1536 / 8, 192, 8, 1, True, False),
                ("imagesMovements/Car1_Ride1536x192.png", self.speed_of_movements_line11, grid_size * 15,
                 y_position_line11 - 12, 1536 / 8, 192, 8, 1, True, False),
                ("imagesMovements/Car2_Ride2048x256.png", self.speed_of_movements_line11, grid_size * 11,
                 y_position_line11 - 12, 2048 / 8, 256, 8, 1, True, False),
                ("imagesMovements/Car2_Ride2048x256.png", self.speed_of_movements_line11, grid_size * 18,
                 y_position_line11 - 12, 2048 / 8, 256, 8, 1, True, False),
                ("imagesMovements/Car3_Ride1536x192.png", self.speed_of_movements_line11, grid_size * 4,
                 y_position_line11 - 12, 1536 / 8, 192, 8, 1, True, False)
            ]
        ]

    def get_movement_data(self):
        return self.movements_data_constructor
