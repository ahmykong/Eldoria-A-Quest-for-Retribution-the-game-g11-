    #damage timer
    self.vulnerable = True
    self.hurt_time = None
    self.invulnerability_duration = 500

    def player_attack_logic(self):
        if self.attack_sprites:
            for attack_sprite in self.attack_sprites:
                collision_sprites = pygame.sprite.sprtecollide(attack_sprite,self.attackable_sprites,False)
                if collision_sprites:
                    for target_sprite in collision_sprites:
                        if target_sprite.sprite_type =='grass':
                            target_sprite.kill()
                        else:
                            target_sprite.get_damage(self.player.attack_sprite.sprite_type)


    def run(self):
        self.player_attack_logic()

    def animate(self):
    #flicker
    if not self.vulnerble:
        alpha = self.wave_value()
        self.image.set_alpha(alpha)
    else:
        self.image.set_alpha(255)

    def damage_player(self,amount,attack_type):
        if self.player.vulnerable:
            self.player.health -= amount
            self.player.vulnerable = False
            self.player.hurt_time = pygame.time.get_ticks()
            # spawn particles

    def cooldown(self):
        if not self.vulnerable:
            if current_time - self.hurt_time >= self.invulnerability_duration:
                self.vulnerable = True