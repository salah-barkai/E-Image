from re import S
from unittest import result
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFlatButton, MDRaisedButton,MDIconButton
from kivymd.uix.textfield import MDTextField, MDTextFieldRect
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
import sqlite3
from kivymd.uix.list import OneLineListItem,TwoLineListItem
from kivymd.icon_definitions import md_icons
from kivy.uix.image import Image
from kivymd.uix.dialog import MDDialog
from kivy.core.window import Window


Window.size=(300, 500)
TABLE_NAME="Emploi_fc1"
TABLE_FC2="Emploi_fc2"
TABLE_SRI1="Emploi_sri1"
TABLE_SRI2="Emploi_sri2"
TABLE_LP="Emploi_lpsri"
TABLE_NAME2="information"
FIELDS=("titre", "contenu")


class app_image(MDApp):
    def build(self):
       self.icon=("LOGO IMAGE.png")
       self.theme_cls.primary_palette= "Blue"
       self.screen=Screen()
       self.image=Image(source="LOGO IMAGE.png", pos_hint={"center_y":.80, "center_x":.5}, size_hint=(.3,.3))
       self.screen.add_widget(self.image)
       self.conn=MDLabel(text="Se connecter", pos_hint={"center_y":.70, "center_x":.5},halign="center", bold=True)
       self.screen.add_widget(self.conn)
       self.Nom=MDTextFieldRect(size_hint=(0.8, None),
                            height="30dp",
                            multiline=False, hint_text="Nom et Prenom",
                            pos_hint={"center_y":.60, "center_x":.5})
       self.screen.add_widget(self.Nom)
       self.Password=MDTextFieldRect(size_hint=(0.8, None),
                            height="30dp",
                            multiline=False, hint_text="Mot de passe",
                            pos_hint={"center_y":.52, "center_x":.5})
       self.screen.add_widget(self.Password)
       self.button=MDRaisedButton(text="Se connecter",
                                  pos_hint={"center_y":.42,"center_x":.5}, 
                                  halign="center",
                                  size_hint=(.65, None), on_release=self.connecter)
       self.screen.add_widget(self.button)
       self.Inscris=MDFlatButton(text="Inscription",
                                  pos_hint={"center_y":.32,"center_x":.5}, 
                                  halign="center",
                                  size_hint=(.65, None), on_release=self.inscription)
       self.screen.add_widget(self.Inscris)
       
       return self.screen
   
    def Home(self,obj):
       self.screen.clear_widgets()
       self.lab=MDLabel(text="Administration",pos_hint={"center_y":.92, "center_x":.5},halign="center", bold=True)
       self.screen.add_widget(self.lab)
       self.fc1=OneLineListItem(text="Modifier emploi du temps FC1" ,pos_hint={"center_y":.85})
       self.fc1.bind(on_release=self.modifier_emploi_fc1)
       self.screen.add_widget(self.fc1)
       self.fc2=OneLineListItem(text="Modifier emploi du temps FC2" ,pos_hint={"center_y":.75})
       self.fc2.bind(on_release=self.modifier_emploi_fc2)
       self.screen.add_widget(self.fc2)
       self.sri1=OneLineListItem(text="Modifier emploi du temps SRI1" ,pos_hint={"center_y":.65})
       self.sri1.bind(on_release=self.modifier_emploi_sri1)
       self.screen.add_widget(self.sri1)
       self.sri2=OneLineListItem(text="Modifier emploi du temps SRI2" ,pos_hint={"center_y":.55})
       self.sri2.bind(on_release=self.modifier_emploi_sri2)
       self.screen.add_widget(self.sri2)
       self.lpsri=OneLineListItem(text="Modifier emploi du temps LP SRI" ,pos_hint={"center_y":.45})
       self.lpsri.bind(on_release=self.modifier_emploi_lp)
       self.screen.add_widget(self.lpsri)
       self.titreinfo=OneLineListItem(text="Partager une information" ,pos_hint={"center_y":.35})
       self.titreinfo.bind(on_release=self.partage_info)
       self.screen.add_widget(self.titreinfo)
       self.box=MDBoxLayout(adaptive_height=True,spacing='57dp', padding='10dp', pos_hint={"center_y":.0},
                              md_bg_color ="blue")
       self.administration=MDIconButton(icon="home",  pos_hint={"center_y":.8}, halign="left",icon_color="white", on_release=self.Home)
       self.box.add_widget(self.administration)
       self.etudiant=MDIconButton(icon="account-school",  pos_hint={"center_y":.8,  "center_x":.5}, halign="center",icon_color="white", on_release=self.Etudiant)
       self.box.add_widget(self.etudiant)
       self.info=MDIconButton(icon="information",  pos_hint={"center_y":.8, "center_x":.89}, halign="right",icon_color="white",on_release=self.Information)
       self.box.add_widget(self.info)
       self.screen.add_widget(self.box)
        
    def connecter(self,obj):
       self.screen.clear_widgets()
       conn=sqlite3.connect("Image.db")
       cursor=conn.cursor()
        
       cursor.execute("SELECT  nom, password FROM inscription")
       results=cursor.fetchall()
       for result in results:
         nom= result[0]
         password= result[1]
         if nom == self.Nom.text and password==self.Password.text:
          self.screen.clear_widgets()
          self.lab=MDLabel(text="Administration",pos_hint={"center_y":.92, "center_x":.5},halign="center", bold=True)
          self.screen.add_widget(self.lab)
          self.fc1=OneLineListItem(text="Modifier emploi du temps FC1" ,pos_hint={"center_y":.85})
          self.fc1.bind(on_release=self.modifier_emploi_fc1)
          self.screen.add_widget(self.fc1)
          self.fc2=OneLineListItem(text="Modifier emploi du temps FC2" ,pos_hint={"center_y":.75})
          self.fc2.bind(on_release=self.modifier_emploi_fc2)
          self.screen.add_widget(self.fc2)
          self.sri1=OneLineListItem(text="Modifier emploi du temps SRI1" ,pos_hint={"center_y":.65})
          self.sri1.bind(on_release=self.modifier_emploi_sri1)
          self.screen.add_widget(self.sri1)
          self.sri2=OneLineListItem(text="Modifier emploi du temps SRI2" ,pos_hint={"center_y":.55})
          self.sri2.bind(on_release=self.modifier_emploi_sri2)
          self.screen.add_widget(self.sri2)
          self.lpsri=OneLineListItem(text="Modifier emploi du temps LP SRI" ,pos_hint={"center_y":.45})
          self.lpsri.bind(on_release=self.modifier_emploi_lp)
          self.screen.add_widget(self.lpsri)
          self.titreinfo=OneLineListItem(text="Partager une information" ,pos_hint={"center_y":.35})
          self.titreinfo.bind(on_release=self.partage_info)
          self.screen.add_widget(self.titreinfo)
          self.box=MDBoxLayout(adaptive_height=True,spacing='57dp', padding='10dp', pos_hint={"center_y":.0},
                              md_bg_color ="blue")
          self.administration=MDIconButton(icon="home",  pos_hint={"center_y":.8}, halign="left",icon_color="white", on_release=self.Home)
          self.box.add_widget(self.administration)
          self.etudiant=MDIconButton(icon="account-school",  pos_hint={"center_y":.8,  "center_x":.5}, halign="center",icon_color="white", on_release=self.Etudiant)
          self.box.add_widget(self.etudiant)
          self.info=MDIconButton(icon="information",  pos_hint={"center_y":.8, "center_x":.89}, halign="right",icon_color="white",on_release=self.Information)
          self.box.add_widget(self.info)
          self.screen.add_widget(self.box)
          break
         else:
            self.screen.clear_widgets()
            print("erreur")
            self.lbl=MDLabel(text="Relancez l'applis avec des vrais identifiant!", pos_hint={"center_y":.70, "center_x":.5},halign="center")
            self.screen.add_widget(self.lbl)
       conn.close()
       
    
    def modifier_emploi_fc1(self, obj):
       self.screen.clear_widgets()
       self.MFtitre=MDLabel(text="Modifier L'emlpoi du Temps", pos_hint={"center_y":.89, "center_x":.5}, halign="center")
       self.screen.add_widget(self.MFtitre)
       self.jour=MDTextFieldRect(size_hint=(0.8, None),
                            height="30dp",
                            multiline=False, hint_text="Jour",
                            pos_hint={"center_y":.79, "center_x":.5})
       self.screen.add_widget(self.jour)
       self.prof=MDTextFieldRect(size_hint=(0.8, None),
                            height="30dp",
                            multiline=False, hint_text="Proffesseur",
                            pos_hint={"center_y":.69, "center_x":.5})
       self.screen.add_widget(self.prof)
       self.matiere=MDTextFieldRect(size_hint=(0.8, None),
                            height="30dp",
                            multiline=False, hint_text="Matiere",
                            pos_hint={"center_y":.59, "center_x":.5})
       self.screen.add_widget(self.matiere)
       self.heure=MDTextFieldRect(size_hint=(0.8, None),
                            height="30dp",
                            multiline=False, hint_text="Heure",
                            pos_hint={"center_y":.49, "center_x":.5})
       self.screen.add_widget(self.heure)
       self.salle=MDTextFieldRect(size_hint=(0.8, None),
                            height="30dp",
                            multiline=False, hint_text="Salle",
                            pos_hint={"center_y":.39, "center_x":.5})
       self.screen.add_widget(self.salle)
       self.button6=MDRaisedButton(text="Modifier", 
                                   pos_hint={"center_y":.19, "center_x":.5}, 
                                   halign="center",size_hint=(.65, None),
                                   )
       self.button6.bind(on_press=self.ajouter_emploi_fc1)
       self.screen.add_widget(self.button6)
       self.text_fields=[self.jour, self.matiere, self.heure,self.prof,self.salle]
       self.box=MDBoxLayout(adaptive_height=True,spacing='57dp', padding='10dp', pos_hint={"center_y":.0},
                              md_bg_color ="blue")
       self.administration=MDIconButton(icon="home",  pos_hint={"center_y":.8}, halign="left",icon_color="white", on_release=self.Home)
       self.box.add_widget(self.administration)
       self.etudiant=MDIconButton(icon="account-school",  pos_hint={"center_y":.8,  "center_x":.5}, halign="center",icon_color="white", on_release=self.Etudiant)
       self.box.add_widget(self.etudiant)
       self.info=MDIconButton(icon="information",  pos_hint={"center_y":.8, "center_x":.89}, halign="right",icon_color="white",on_relase=self.Information)
       self.box.add_widget(self.info)
       self.screen.add_widget(self.box)
    
    def modifier_emploi_fc2(self, obj):
       self.screen.clear_widgets()
       self.MFtitre=MDLabel(text="Modifier L'emlpoi du Temps", pos_hint={"center_y":.89, "center_x":.5}, halign="center")
       self.screen.add_widget(self.MFtitre)
       self.jourfc2=MDTextFieldRect(size_hint=(0.8, None),
                            height="30dp",
                            multiline=False, hint_text="Jour",
                            pos_hint={"center_y":.79, "center_x":.5})
       self.screen.add_widget(self.jourfc2)
       self.proffc2=MDTextFieldRect(size_hint=(0.8, None),
                            height="30dp",
                            multiline=False, hint_text="Proffesseur",
                            pos_hint={"center_y":.69, "center_x":.5})
       self.screen.add_widget(self.proffc2)
       self.matierefc2=MDTextFieldRect(size_hint=(0.8, None),
                            height="30dp",
                            multiline=False, hint_text="Matiere",
                            pos_hint={"center_y":.59, "center_x":.5})
       self.screen.add_widget(self.matierefc2)
       self.heurefc2=MDTextFieldRect(size_hint=(0.8, None),
                            height="30dp",
                            multiline=False, hint_text="Heure",
                            pos_hint={"center_y":.49, "center_x":.5})
       self.screen.add_widget(self.heurefc2)
       self.sallefc2=MDTextFieldRect(size_hint=(0.8, None),
                            height="30dp",
                            multiline=False, hint_text="Salle",
                            pos_hint={"center_y":.39, "center_x":.5})
       self.screen.add_widget(self.sallefc2)
       self.button6=MDRaisedButton(text="Modifier", 
                                   pos_hint={"center_y":.19, "center_x":.5}, 
                                   halign="center",size_hint=(.65, None),
                                   )
       self.button6.bind(on_press=self.ajouter_emploi_fc2)
       self.screen.add_widget(self.button6)
       self.text_fields=[self.jour, self.matiere, self.heure,self.prof,self.salle]
       self.box=MDBoxLayout(adaptive_height=True,spacing='57dp', padding='10dp', pos_hint={"center_y":.0},
                              md_bg_color ="blue")
       self.administration=MDIconButton(icon="home",  pos_hint={"center_y":.8}, halign="left",icon_color="white", on_release=self.Home)
       self.box.add_widget(self.administration)
       self.etudiant=MDIconButton(icon="account-school",  pos_hint={"center_y":.8,  "center_x":.5}, halign="center",icon_color="white", on_release=self.Etudiant)
       self.box.add_widget(self.etudiant)
       self.info=MDIconButton(icon="information",  pos_hint={"center_y":.8, "center_x":.89}, halign="right",icon_color="white",on_relase=self.Information)
       self.box.add_widget(self.info)
       self.screen.add_widget(self.box)
    
    def modifier_emploi_sri1(self, obj):
       self.screen.clear_widgets()
       self.MFtitre=MDLabel(text="Modifier L'emlpoi du Temps", pos_hint={"center_y":.89, "center_x":.5}, halign="center")
       self.screen.add_widget(self.MFtitre)
       self.joursri1=MDTextFieldRect(size_hint=(0.8, None),
                            height="30dp",
                            multiline=False, hint_text="Jour",
                            pos_hint={"center_y":.79, "center_x":.5})
       self.screen.add_widget(self.joursri1)
       self.profsri1=MDTextFieldRect(size_hint=(0.8, None),
                            height="30dp",
                            multiline=False, hint_text="Proffesseur",
                            pos_hint={"center_y":.69, "center_x":.5})
       self.screen.add_widget(self.profsri1)
       self.matieresri1=MDTextFieldRect(size_hint=(0.8, None),
                            height="30dp",
                            multiline=False, hint_text="Matiere",
                            pos_hint={"center_y":.59, "center_x":.5})
       self.screen.add_widget(self.matieresri1)
       self.heuresri1=MDTextFieldRect(size_hint=(0.8, None),
                            height="30dp",
                            multiline=False, hint_text="Heure",
                            pos_hint={"center_y":.49, "center_x":.5})
       self.screen.add_widget(self.heuresri1)
       self.sallesri1=MDTextFieldRect(size_hint=(0.8, None),
                            height="30dp",
                            multiline=False, hint_text="Salle",
                            pos_hint={"center_y":.39, "center_x":.5})
       self.screen.add_widget(self.sallesri1)
       self.button6=MDRaisedButton(text="Modifier", 
                                   pos_hint={"center_y":.19, "center_x":.5}, 
                                   halign="center",size_hint=(.65, None),
                                   )
       self.button6.bind(on_press=self.ajouter_emploi_sri1)
       self.screen.add_widget(self.button6)
       self.text_fields=[self.jour, self.matiere, self.heure,self.prof,self.salle]
       self.box=MDBoxLayout(adaptive_height=True,spacing='57dp', padding='10dp', pos_hint={"center_y":.0},
                              md_bg_color ="blue")
       self.administration=MDIconButton(icon="home",  pos_hint={"center_y":.8}, halign="left",icon_color="white", on_release=self.Home)
       self.box.add_widget(self.administration)
       self.etudiant=MDIconButton(icon="account-school",  pos_hint={"center_y":.8,  "center_x":.5}, halign="center",icon_color="white", on_release=self.Etudiant)
       self.box.add_widget(self.etudiant)
       self.info=MDIconButton(icon="information",  pos_hint={"center_y":.8, "center_x":.89}, halign="right",icon_color="white",on_relase=self.Information)
       self.box.add_widget(self.info)
       self.screen.add_widget(self.box)
    
    def modifier_emploi_sri2(self, obj):
       self.screen.clear_widgets()
       self.MFtitre=MDLabel(text="Modifier L'emlpoi du Temps", pos_hint={"center_y":.89, "center_x":.5}, halign="center")
       self.screen.add_widget(self.MFtitre)
       self.joursri2=MDTextFieldRect(size_hint=(0.8, None),
                            height="30dp",
                            multiline=False, hint_text="Jour",
                            pos_hint={"center_y":.79, "center_x":.5})
       self.screen.add_widget(self.joursri2)
       self.profsri2=MDTextFieldRect(size_hint=(0.8, None),
                            height="30dp",
                            multiline=False, hint_text="Proffesseur",
                            pos_hint={"center_y":.69, "center_x":.5})
       self.screen.add_widget(self.profsri2)
       self.matieresri2=MDTextFieldRect(size_hint=(0.8, None),
                            height="30dp",
                            multiline=False, hint_text="Matiere",
                            pos_hint={"center_y":.59, "center_x":.5})
       self.screen.add_widget(self.matieresri2)
       self.heuresri2=MDTextFieldRect(size_hint=(0.8, None),
                            height="30dp",
                            multiline=False, hint_text="Heure",
                            pos_hint={"center_y":.49, "center_x":.5})
       self.screen.add_widget(self.heuresri2)
       self.sallesri2=MDTextFieldRect(size_hint=(0.8, None),
                            height="30dp",
                            multiline=False, hint_text="Salle",
                            pos_hint={"center_y":.39, "center_x":.5})
       self.screen.add_widget(self.sallesri2)
       self.button6=MDRaisedButton(text="Modifier", 
                                   pos_hint={"center_y":.19, "center_x":.5}, 
                                   halign="center",size_hint=(.65, None),
                                   )
       self.button6.bind(on_press=self.ajouter_emploi_sri2)
       self.screen.add_widget(self.button6)
       self.text_fields=[self.jour, self.matiere, self.heure,self.prof,self.salle]
       self.box=MDBoxLayout(adaptive_height=True,spacing='57dp', padding='10dp', pos_hint={"center_y":.0},
                              md_bg_color ="blue")
       self.administration=MDIconButton(icon="home",  pos_hint={"center_y":.8}, halign="left",icon_color="white", on_release=self.Home)
       self.box.add_widget(self.administration)
       self.etudiant=MDIconButton(icon="account-school",  pos_hint={"center_y":.8,  "center_x":.5}, halign="center",icon_color="white", on_release=self.Etudiant)
       self.box.add_widget(self.etudiant)
       self.info=MDIconButton(icon="information",  pos_hint={"center_y":.8, "center_x":.89}, halign="right",icon_color="white",on_relase=self.Information)
       self.box.add_widget(self.info)
       self.screen.add_widget(self.box)
       
    def modifier_emploi_lp(self, obj):
       self.screen.clear_widgets()
       self.MFtitre=MDLabel(text="Modifier L'emlpoi du Temps", pos_hint={"center_y":.89, "center_x":.5}, halign="center")
       self.screen.add_widget(self.MFtitre)
       self.jourlp=MDTextFieldRect(size_hint=(0.8, None),
                            height="30dp",
                            multiline=False, hint_text="Jour",
                            pos_hint={"center_y":.79, "center_x":.5})
       self.screen.add_widget(self.jourlp)
       self.proflp=MDTextFieldRect(size_hint=(0.8, None),
                            height="30dp",
                            multiline=False, hint_text="Proffesseur",
                            pos_hint={"center_y":.69, "center_x":.5})
       self.screen.add_widget(self.proflp)
       self.matierelp=MDTextFieldRect(size_hint=(0.8, None),
                            height="30dp",
                            multiline=False, hint_text="Matiere",
                            pos_hint={"center_y":.59, "center_x":.5})
       self.screen.add_widget(self.matierelp)
       self.heurelp=MDTextFieldRect(size_hint=(0.8, None),
                            height="30dp",
                            multiline=False, hint_text="Heure",
                            pos_hint={"center_y":.49, "center_x":.5})
       self.screen.add_widget(self.heurelp)
       self.sallelp=MDTextFieldRect(size_hint=(0.8, None),
                            height="30dp",
                            multiline=False, hint_text="Salle",
                            pos_hint={"center_y":.39, "center_x":.5})
       self.screen.add_widget(self.sallelp)
       self.button6=MDRaisedButton(text="Modifier", 
                                   pos_hint={"center_y":.19, "center_x":.5}, 
                                   halign="center",size_hint=(.65, None),
                                   )
       self.button6.bind(on_press=self.ajouter_emploi_lp)
       self.screen.add_widget(self.button6)
       self.text_fields=[self.jour, self.matiere, self.heure,self.prof,self.salle]
       self.box=MDBoxLayout(adaptive_height=True,spacing='57dp', padding='10dp', pos_hint={"center_y":.0},
                              md_bg_color ="blue")
       self.administration=MDIconButton(icon="home",  pos_hint={"center_y":.8}, halign="left",icon_color="white", on_release=self.Home)
       self.box.add_widget(self.administration)
       self.etudiant=MDIconButton(icon="account-school",  pos_hint={"center_y":.8,  "center_x":.5}, halign="center",icon_color="white", on_release=self.Etudiant)
       self.box.add_widget(self.etudiant)
       self.info=MDIconButton(icon="information",  pos_hint={"center_y":.8, "center_x":.89}, halign="right",icon_color="white",on_relase=self.Information)
       self.box.add_widget(self.info)
       self.screen.add_widget(self.box)
    
    def Etudiant(self, obj):
       self.screen.clear_widgets()
       self.image=Image(source="LOGO IMAGE.png", pos_hint={"center_y":.92, "center_x":.5}, size_hint=(.3,.3))
       self.screen.add_widget(self.image)
       self.titre=MDLabel(text="Emplois des temps", pos_hint={"center_y":.82, "center_x":.5},halign="center", bold=True)
       self.buttonf1=MDRaisedButton(text="Finance Année 1",
                                  pos_hint={"center_y":.70,"center_x":.5}, 
                                  halign="center",
                                  size_hint=(.65, None), on_release=self.emploi_fc1)
       self.buttonf2=MDRaisedButton(text="Finance Année 2",
                                  pos_hint={"center_y":.60,"center_x":.5}, 
                                  halign="center",
                                  size_hint=(.65, None), on_release=self.emploi_fc2)
       self.buttonsri1=MDRaisedButton(text="SRI Anneé 1",
                                  pos_hint={"center_y":.50,"center_x":.5}, 
                                  halign="center",
                                  size_hint=(.65, None), on_release=self.emploi_sri1)
       self.buttonsri2=MDRaisedButton(text="SRI Anneé 2",
                                  pos_hint={"center_y":.40,"center_x":.5}, 
                                  halign="center",
                                  size_hint=(.65, None), on_release=self.emploi_sri2)
       self.buttonlpsri=MDRaisedButton(text="Lp SRI",
                                  pos_hint={"center_y":.30,"center_x":.5}, 
                                  halign="center",
                                  size_hint=(.65, None), on_release=self.emploi_lp)
       self.screen.add_widget(self.titre)
       self.screen.add_widget(self.buttonf1)
       self.screen.add_widget(self.buttonf2)
       self.screen.add_widget(self.buttonsri1)
       self.screen.add_widget(self.buttonsri2)
       self.screen.add_widget(self.buttonlpsri)
       self.box=MDBoxLayout(adaptive_height=True,spacing='57dp', padding='10dp', pos_hint={"center_y":.0},
                              md_bg_color ="blue")
       self.administration=MDIconButton(icon="home",  pos_hint={"center_y":.8}, halign="left",icon_color="white", on_release=self.Home)
       self.box.add_widget(self.administration)
       self.etudiant=MDIconButton(icon="account-school",  pos_hint={"center_y":.8,  "center_x":.5}, halign="center",icon_color="white", on_release=self.Etudiant)
       self.box.add_widget(self.etudiant)
       self.info=MDIconButton(icon="information",  pos_hint={"center_y":.8, "center_x":.89}, halign="right",icon_color="white",on_release=self.Information)
       self.box.add_widget(self.info)
       self.screen.add_widget(self.box)
       
    
  
    def ajouter_emploi_fc1(self, instance):
           jour=self.jour.text
           matiere=self.matiere.text
           heure=self.heure.text
           prof=self.prof.text
           salle=self.salle.text
           con = sqlite3.connect('Image.db')
           cuser = con.cursor()
           cuser.execute("""insert into Emploi_fc1(
            "jour",
            "matiere",
            "heure",
            "prof",
            "salle"
             ) values(?,?,?,?,?)""", (jour,matiere,heure,prof,salle))
           con.commit()
           con.close()
           
    def ajouter_emploi_lp(self, instance):
           jour=self.jourlp.text
           matiere=self.matierelp.text
           heure=self.heurelp.text
           prof=self.proflp.text
           salle=self.sallelp.text
           con = sqlite3.connect('Image.db')
           cuser = con.cursor()
           cuser.execute("""insert into Emploi_lpsri(
            "jour",
            "matiere",
            "heure",
            "prof",
            "salle"
             ) values(?,?,?,?,?)""", (jour,matiere,heure,prof,salle))
           con.commit()
           con.close()
           
    def ajouter_emploi_fc2(self, instance):
           jour=self.jourfc2.text
           matiere=self.matierefc2.text
           heure=self.heurefc2.text
           prof=self.proffc2.text
           salle=self.sallefc2.text
           con = sqlite3.connect('Image.db')
           cuser = con.cursor()
           cuser.execute("""insert into Emploi_fc2(
            "jour",
            "matiere",
            "heure",
            "prof",
            "salle"
             ) values(?,?,?,?,?)""", (jour,matiere,heure,prof,salle))
           con.commit()
           con.close()
           
    def ajouter_emploi_sri2(self, instance):
           jour=self.joursri2.text
           matiere=self.matieresri2.text
           heure=self.heuresri2.text
           prof=self.profsri2.text
           salle=self.sallesri2.text
           con = sqlite3.connect('Image.db')
           cuser = con.cursor()
           cuser.execute("""insert into Emploi_sri2(
            "jour",
            "matiere",
            "heure",
            "prof",
            "salle"
             ) values(?,?,?,?,?)""", (jour,matiere,heure,prof,salle))
           con.commit()
           con.close()
    def ajouter_emploi_sri1(self, instance):
           jour=self.joursri1.text
           matiere=self.matieresri1.text
           heure=self.heuresri1.text
           prof=self.profsri1.text
           salle=self.sallesri1.text
           con = sqlite3.connect('Image.db')
           cuser = con.cursor()
           cuser.execute("""insert into Emploi_sri1(
            "jour",
            "matiere",
            "heure",
            "prof",
            "salle"
             ) values(?,?,?,?,?)""", (jour,matiere,heure,prof,salle))
           con.commit()
           con.close()

    def emploi_fc1(self,obj):
        
         # Charger les données depuis la base de données et les afficher dans la DataTable
        conn = sqlite3.connect("Image.db")
        c = conn.cursor()
        c.execute(f"SELECT * FROM {TABLE_NAME}")
        data = c.fetchall()
        conn.close()
        self.rows = []
        for row in data:
          self.rows.append([str(value) for value in row])
          
        self.screen.clear_widgets()
        self.table= MDDataTable(size_hint=(0.9,0.6),
          pos_hint={"center_y":.70,"center_x":.5},
            column_data=[
           ("Jour", dp(11)),
           ("Matiere", dp(15)),
           ("Heure", dp(11)),
           ("Prof", dp(12)),
           ("Salle", dp(10))
           ],row_data=self.rows
            )
        self.screen.add_widget(self.table)
        self.box=MDBoxLayout(adaptive_height=True,spacing='57dp', padding='10dp', pos_hint={"center_y":.0},
                              md_bg_color ="blue")
        self.administration=MDIconButton(icon="home",  pos_hint={"center_y":.8}, halign="left",icon_color="white", on_release=self.Home)
        self.box.add_widget(self.administration)
        self.etudiant=MDIconButton(icon="account-school",  pos_hint={"center_y":.8,  "center_x":.5}, halign="center",icon_color="white", on_release=self.Etudiant)
        self.box.add_widget(self.etudiant)
        self.info=MDIconButton(icon="information",  pos_hint={"center_y":.8, "center_x":.89}, halign="right",icon_color="white")
        self.box.add_widget(self.info)
        self.screen.add_widget(self.box)
        
    def emploi_fc2(self,obj):
            
         # Charger les données depuis la base de données et les afficher dans la DataTable
        conn = sqlite3.connect("Image.db")
        c = conn.cursor()
        c.execute(f"SELECT * FROM {TABLE_FC2}")
        data = c.fetchall()
        conn.close()
        self.rows = []
        for row in data:
          self.rows.append([str(value) for value in row])
          
        self.screen.clear_widgets()
        self.table= MDDataTable(size_hint=(0.9,0.6),
          pos_hint={"center_y":.70,"center_x":.5},
            column_data=[
           ("Jour", dp(11)),
           ("Matiere", dp(15)),
           ("Heure", dp(11)),
           ("Prof", dp(12)),
           ("Salle", dp(10))
           ],row_data=self.rows
            )
        self.screen.add_widget(self.table)
        self.box=MDBoxLayout(adaptive_height=True,spacing='57dp', padding='10dp', pos_hint={"center_y":.0},
                              md_bg_color ="blue")
        self.administration=MDIconButton(icon="home",  pos_hint={"center_y":.8}, halign="left",icon_color="white", on_release=self.Home)
        self.box.add_widget(self.administration)
        self.etudiant=MDIconButton(icon="account-school",  pos_hint={"center_y":.8,  "center_x":.5}, halign="center",icon_color="white", on_release=self.Etudiant)
        self.box.add_widget(self.etudiant)
        self.info=MDIconButton(icon="information",  pos_hint={"center_y":.8, "center_x":.89}, halign="right",icon_color="white")
        self.box.add_widget(self.info)
        self.screen.add_widget(self.box)
    
    def emploi_sri1(self,obj):
            
         # Charger les données depuis la base de données et les afficher dans la DataTable
        conn = sqlite3.connect("Image.db")
        c = conn.cursor()
        c.execute(f"SELECT * FROM {TABLE_SRI1}")
        data = c.fetchall()
        conn.close()
        self.rows = []
        for row in data:
          self.rows.append([str(value) for value in row])
          
        self.screen.clear_widgets()
        self.table= MDDataTable(size_hint=(0.9,0.6),
          pos_hint={"center_y":.70,"center_x":.5},
            column_data=[
           ("Jour", dp(11)),
           ("Matiere", dp(15)),
           ("Heure", dp(11)),
           ("Prof", dp(12)),
           ("Salle", dp(10))
           ],row_data=self.rows
            )
        self.screen.add_widget(self.table)
        self.box=MDBoxLayout(adaptive_height=True,spacing='57dp', padding='10dp', pos_hint={"center_y":.0},
                              md_bg_color ="blue")
        self.administration=MDIconButton(icon="home",  pos_hint={"center_y":.8}, halign="left",icon_color="white", on_release=self.Home)
        self.box.add_widget(self.administration)
        self.etudiant=MDIconButton(icon="account-school",  pos_hint={"center_y":.8,  "center_x":.5}, halign="center",icon_color="white", on_release=self.Etudiant)
        self.box.add_widget(self.etudiant)
        self.info=MDIconButton(icon="information",  pos_hint={"center_y":.8, "center_x":.89}, halign="right",icon_color="white")
        self.box.add_widget(self.info)
        self.screen.add_widget(self.box)
        
    def emploi_sri2(self,obj):
            
         # Charger les données depuis la base de données et les afficher dans la DataTable
        conn = sqlite3.connect("Image.db")
        c = conn.cursor()
        c.execute(f"SELECT * FROM {TABLE_SRI2}")
        data = c.fetchall()
        conn.close()
        self.rows = []
        for row in data:
          self.rows.append([str(value) for value in row])
          
        self.screen.clear_widgets()
        self.table= MDDataTable(size_hint=(0.9,0.6),
          pos_hint={"center_y":.70,"center_x":.5},
            column_data=[
           ("Jour", dp(11)),
           ("Matiere", dp(15)),
           ("Heure", dp(11)),
           ("Prof", dp(12)),
           ("Salle", dp(10))
           ],row_data=self.rows
            )
        self.screen.add_widget(self.table)
        self.box=MDBoxLayout(adaptive_height=True,spacing='57dp', padding='10dp', pos_hint={"center_y":.0},
                              md_bg_color ="blue")
        self.administration=MDIconButton(icon="home",  pos_hint={"center_y":.8}, halign="left",icon_color="white", on_release=self.Home)
        self.box.add_widget(self.administration)
        self.etudiant=MDIconButton(icon="account-school",  pos_hint={"center_y":.8,  "center_x":.5}, halign="center",icon_color="white", on_release=self.Etudiant)
        self.box.add_widget(self.etudiant)
        self.info=MDIconButton(icon="information",  pos_hint={"center_y":.8, "center_x":.89}, halign="right",icon_color="white")
        self.box.add_widget(self.info)
        self.screen.add_widget(self.box)
        
    def emploi_lp(self,obj):
            
         # Charger les données depuis la base de données et les afficher dans la DataTable
        conn = sqlite3.connect("Image.db")
        c = conn.cursor()
        c.execute(f"SELECT * FROM {TABLE_LP}")
        data = c.fetchall()
        conn.close()
        self.rows = []
        for row in data:
          self.rows.append([str(value) for value in row])
          
        self.screen.clear_widgets()
        self.table= MDDataTable(size_hint=(0.9,0.6),
          pos_hint={"center_y":.70,"center_x":.5},
            column_data=[
           ("Jour", dp(11)),
           ("Matiere", dp(15)),
           ("Heure", dp(11)),
           ("Prof", dp(12)),
           ("Salle", dp(10))
           ],row_data=self.rows
            )
        self.screen.add_widget(self.table)
        self.box=MDBoxLayout(adaptive_height=True,spacing='57dp', padding='10dp', pos_hint={"center_y":.0},
                              md_bg_color ="blue")
        self.administration=MDIconButton(icon="home",  pos_hint={"center_y":.8}, halign="left",icon_color="white", on_release=self.Home)
        self.box.add_widget(self.administration)
        self.etudiant=MDIconButton(icon="account-school",  pos_hint={"center_y":.8,  "center_x":.5}, halign="center",icon_color="white", on_release=self.Etudiant)
        self.box.add_widget(self.etudiant)
        self.info=MDIconButton(icon="information",  pos_hint={"center_y":.8, "center_x":.89}, halign="right",icon_color="white")
        self.box.add_widget(self.info)
        self.screen.add_widget(self.box)
    
    def Information(self, obj):
       self.screen.clear_widgets()
       self.lab=MDLabel(text="Information",pos_hint={"center_y":.92, "center_x":.5},halign="center", bold=True)
       self.screen.add_widget(self.lab)
       self.titreemploif=OneLineListItem(text="Information de l'ecole" ,pos_hint={"center_y":.85})
       self.titreemploif.bind(on_release=self.afficher_info)
       self.screen.add_widget(self.titreemploif)
       self.titreinfo=OneLineListItem(text="Partager une information" ,pos_hint={"center_y":.75})
       self.titreinfo.bind(on_release=self.partage_info)
       self.screen.add_widget(self.titreinfo)
       self.box=MDBoxLayout(adaptive_height=True,spacing='57dp', padding='10dp', pos_hint={"center_y":.0},
                              md_bg_color ="blue")
       self.administration=MDIconButton(icon="home",  pos_hint={"center_y":.8}, halign="left",icon_color="white", on_release=self.Home)
       self.box.add_widget(self.administration)
       self.etudiant=MDIconButton(icon="account-school",  pos_hint={"center_y":.8,  "center_x":.5}, halign="center",icon_color="white", on_release=self.Etudiant)
       self.box.add_widget(self.etudiant)
       self.info=MDIconButton(icon="information",  pos_hint={"center_y":.8, "center_x":.89}, halign="right",icon_color="white",on_release=self.Information)
       self.box.add_widget(self.info)
       self.screen.add_widget(self.box)
    
    def partage_info(self, obj):
        self.screen.clear_widgets()
        self.label1=MDLabel(text=("Partager une Informatique"), pos_hint={"center_y":.80, "center_x":.5},halign="center")
        self.screen.add_widget(self.label1)
        self.Titre0=MDTextFieldRect(size_hint=(0.8, None),
                            height="30dp",
                            multiline=False, hint_text="Titre d'information",
                            pos_hint={"center_y":.70, "center_x":.5})
        self.screen.add_widget(self.Titre0)
        self.contenu=MDTextFieldRect(size_hint=(0.8, .3),
                            height="30dp",
                            multiline=False, hint_text="Contenu d'information",
                            pos_hint={"center_y":.45, "center_x":.5})
        self.screen.add_widget(self.contenu)
        self.envoie=MDRaisedButton(text="Envoyez",pos_hint={"center_y":.22, "center_x":.5},halign="center", on_release=self.enregistrer_info)
        self.screen.add_widget(self.envoie)
        self.box=MDBoxLayout(adaptive_height=True,spacing='57dp', padding='10dp', pos_hint={"center_y":.0},
                              md_bg_color ="blue")
        self.administration=MDIconButton(icon="home",  pos_hint={"center_y":.8}, halign="left",icon_color="white", on_release=self.Home)
        self.box.add_widget(self.administration)
        self.etudiant=MDIconButton(icon="account-school",  pos_hint={"center_y":.8,  "center_x":.5}, halign="center",icon_color="white", on_release=self.Etudiant)
        self.box.add_widget(self.etudiant)
        self.info=MDIconButton(icon="information",  pos_hint={"center_y":.8, "center_x":.89}, halign="right",icon_color="white",on_release=self.Information)
        self.box.add_widget(self.info)
        self.screen.add_widget(self.box)
        
    
    def enregistrer_info(self, obj):
           titre=self.Titre0.text
           contenu=self.contenu.text
           con = sqlite3.connect('Image.db')
           cuser = con.cursor()
           cuser.execute("""insert into information(
            "titre",
            "contenu"
            ) values(?,?)""", (titre,contenu))
           con.commit()
           con.close()

    def afficher_info(self,obj):
        # Charger les données depuis la base de données et les afficher dans la DataTable
        conn = sqlite3.connect("Image.db")
        c = conn.cursor()
        c.execute(f"SELECT {', '.join(FIELDS)} FROM {TABLE_NAME2}")
        data = c.fetchall()
        conn.close()
        for info in data:
            titre_label=TwoLineListItem(text=info[0],secondary_text=info[1], pos_hint={"center_y":.78, "center_x":.5})
            self.screen.clear_widgets()
            self.screen.add_widget(titre_label)
        self.lab=MDLabel(text="Information",pos_hint={"center_y":.92, "center_x":.5},halign="center", bold=True)
        self.screen.add_widget(self.lab)
        self.box=MDBoxLayout(adaptive_height=True,spacing='57dp', padding='10dp', pos_hint={"center_y":.0},
                              md_bg_color ="blue")
        self.administration=MDIconButton(icon="home",  pos_hint={"center_y":.8}, halign="left",icon_color="white", on_release=self.Home)
        self.box.add_widget(self.administration)
        self.etudiant=MDIconButton(icon="account-school",  pos_hint={"center_y":.8,  "center_x":.5}, halign="center",icon_color="white", on_release=self.Etudiant)
        self.box.add_widget(self.etudiant)
        self.info=MDIconButton(icon="information",  pos_hint={"center_y":.8, "center_x":.89}, halign="right",icon_color="white",on_release=self.Information)
        self.box.add_widget(self.info)
        self.screen.add_widget(self.box)
            
    def enregistrer_inscris(self):
           nom=self.Nom.text
           prenom=self.Prenom.text
           password=self.Password.text
           con = sqlite3.connect('Image.db')
           cuser = con.cursor()
           cuser.execute("""insert into inscription(
            "nom",
            "prenom",
            "password"
            ) values(?,?,?)""", (nom,prenom,password))
           con.commit()
           con.close()    
     
        
    
    def inscription(self,obj):
       self.screen.clear_widgets()
       self.titre=MDLabel(text="Institut IMAGE", pos_hint={"center_y":.85, "center_x":.5},halign="center", bold=True)
       self.screen.add_widget(self.titre)
       self.Nom=MDTextFieldRect(size_hint=(0.8, None),
                            height="30dp",
                            multiline=False, hint_text="Nom",
                            pos_hint={"center_y":.75, "center_x":.5})
       self.screen.add_widget(self.Nom)
       self.Prenom=MDTextFieldRect(size_hint=(0.8, None),
                            height="30dp",
                            multiline=False, hint_text="Prenom",
                            pos_hint={"center_y":.65, "center_x":.5})
       self.screen.add_widget(self.Prenom)
       self.Password=MDTextFieldRect(size_hint=(0.8, None),
                            height="30dp",
                            multiline=False, hint_text="Mot de passe",
                            pos_hint={"center_y":.55, "center_x":.5})
       self.screen.add_widget(self.Password)
       self.confirmation=MDTextFieldRect(size_hint=(0.8, None),
                            height="30dp",
                            multiline=False, hint_text="Confirmation",
                            pos_hint={"center_y":.45, "center_x":.5})
       self.screen.add_widget(self.confirmation)
       self.button=MDRaisedButton(text="S'inscrire",
                                  pos_hint={"center_y":.35,"center_x":.5}, 
                                  halign="center",
                                  size_hint=(.65, None), on_release=self.on_button)
       self.screen.add_widget(self.button)
       self.button=MDFlatButton(text="Se connecter",
                                  pos_hint={"center_y":.25,"center_x":.5}, 
                                  halign="center",
                                  size_hint=(.65, None), on_release=self.inscris_connecter)
       self.screen.add_widget(self.button)
       
       
    def check_connection(self):
        conn=sqlite3.connect("Image.db")
        cursor=conn.cursor()
        
        cursor.execute("SELECT * FROM inscription WHERE nom=? AND password=?",(self.nom,self.password))
        result=cursor.fetchone()
        
        conn.close()
        if result:
            pass
        else:
            print("erreur")
    
    def inscris_connecter(self, obj):
       self.screen.clear_widgets()
       self.image=Image(source="LOGO IMAGE.png", pos_hint={"center_y":.80, "center_x":.5}, size_hint=(.3,.3))
       self.screen.add_widget(self.image)
       self.conn=MDLabel(text="Se connecter", pos_hint={"center_y":.70, "center_x":.5},halign="center", bold=True)
       self.screen.add_widget(self.conn)
       self.Nom=MDTextFieldRect(size_hint=(0.8, None),
                            height="30dp",
                            multiline=False, hint_text="Nom et Prenom",
                            pos_hint={"center_y":.60, "center_x":.5})
       self.screen.add_widget(self.Nom)
       self.Password=MDTextFieldRect(size_hint=(0.8, None),
                            height="30dp",
                            multiline=False, hint_text="Mot de passe",
                            pos_hint={"center_y":.52, "center_x":.5})
       self.screen.add_widget(self.Password)
       self.button=MDRaisedButton(text="Se connecter",
                                  pos_hint={"center_y":.42,"center_x":.5}, 
                                  halign="center",
                                  size_hint=(.65, None), on_release=self.connecter)
       self.screen.add_widget(self.button)
       
    def on_button(self, obj):
        self.show_dialog()
        self.enregistrer_inscris()
       
    def show_dialog(self):
        
        self.dialog = MDDialog(
                title="Inscription",
                text="Félicitation vous etes bien inscris!",
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        on_release=self.close_dialog
                    ),
                    MDFlatButton(
                        text="OK",
                        on_release=self.close_dialog
                    ),
                ],
            )
        self.dialog.open()

    def close_dialog(self, *args):
        self.dialog.dismiss()
       
      
   
    
    
    
    
    





app= app_image()
app.run()
    
        
 