# You can place your game script in this file.

#Variables
init:

    define slow_dissolve = Dissolve(5.0)


    transform camera_chest_to_waist:  # New transformation for belt level
        yanchor 0.25
        linear 5.0 yanchor 0.66  # Change duration and end position as needed


    transform camera_head_to_chest:
        zoom 3.0
        xalign 0.5
        yalign 0.5
        yanchor 0.0
        linear 15.0 yanchor 0.25
        
   
init python:
    # Function to automatically stop sound
    def change_background_with_sound_interrupt(background):
        renpy.sound.stop()
        renpy.show(background)


transform half_size_northeast:
    zoom 0.3
    xalign 0.7
    yalign 0.3      

transform half_size_northeast2:
    zoom 0.6
    xalign 0.7
    yalign 0.9       

python:
    scene.camera.dolly(kuro_lamia, 1.0)  # Move the camera to the character kuro_lamia

# Definition of game characters.
define r = Character('ナレーター', color="#c8ffc8")
define シラン = Character('シラン', color="#ffffff")
define lam = Character('ダークラミア', color="#460c00")

# Instead of using the image operator, you can simply
# put all your image files in the images folder.
# For example, the bg room scene can be called by the file "bg room.png",
# and eileen happy - "eileen happy.webp", and then they will appear in the game.

# Muzon
define audio.koster = "music/01_koster.mp3"
define audio.forest = "music/02_nochnogo_lesa.mp3"
define audio.river = "music/03_river.mp3"
define audio.happy = "music/happy_theme.mp3"
define audio.wind = "music/night_wind.mp3"
define audio.terror01 = "music/terror.ogg"

# Sounds
define audio.heart = "audio/sound/heartbeat.mp3"
define audio.hit = "audio/sound/udar-dubinok.ogg"
define audio.fall = "audio/sound/padenie_tela.mp3"

# Effects
image blood = "/images/bg/blood.png"

# Main menu


# The game starts here:

label start:

    "{color=#FF0000}こんにちは、ゲームのアルファバージョンにご参加いただき、\nありがとうございます！{/color}"
    "{color=#FF0000}このバージョンはまだ開発中であり、今後さらに改善やアップデートが\n行われます。{/color}"
    "{color=#FF0000}ゲームをプレイしながらのフィードバックは非常に重要で、\nゲームの品質向上に役立ちます。{/color}"
    "{color=#FF0000}どんなご意見やご要望でもお気軽にお知らせください。\nお力をお貸しいただき、ありがとうございます。{/color}"
    "{color=#FF0000}引き続きお楽しみください！"
    
    play music koster
    
    scene arena_bg

    show main_chara_mini

    r "親愛なる友人の皆さん、ようこそ！ 今日は、古代の世界で始まった\nエキサイティングな物語をお話ししましょう。"

    r "この物語は、2100年前に古代の世界で始まりました。"

    r "物語は、古代ローマ帝国の国境に位置する暗い森から始まります。\n当時、帝国は急速に拡大し、その支配は多くの土地に及んでいました。"

    r "しかし、その支配に不満を抱いた土地もありました。\nイベリアの州では反乱が勃発し、ローマにとって本気の試練\nとなりました。"

    r "自由と独立を求めて立ち上がったイベリア人たちは、ローマ帝国に挑戦\nしました。反乱軍の指導者たちは自由への渇望に駆られ、普通の人々から強力なローマ軍団と戦うために軍を結成しました。"

    r "ローマは反乱を鎮圧するために自信たっぷりの軍団を送りましたが、\n彼らには予想外の激戦と損失が待っていました。"

    r "長い間敗北を知らなかったローマ軍団は、イベリア人たちの決意と地理的な知識と対峙しました。自分たちの土地を守るために立ち上がった\nイベリア人たちは、ローマ軍団に深刻な打撃を与えました。"

    r "イベリアの闘争はローマ帝国に深刻な危機をもたらしました。\n遠く離れた目立たない州が、帝国に深刻な頭痛を引き起こす\n要因となりました。"

    r "歴史の舞台がここから始まり、イベリアの自由とその帝国への影響が背景にあります。"

    r "登場人物、彼らの物語、そして多くの人々の運命を決定する選択について詳しく学びましょう。過去へのエキサイティングな旅に備え、ローマ帝国とその州の未来を左右する難しい決断に備えてください。"   
    
    stop music
    
    scene forest_bg with slow_dissolve

    play music happy
    $ player_name = renpy.input("Enter the main character's name")
    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name = "勇者"
    $ player = Character(player_name)
    
    player "私達は今3日間行っています。 なぜこの森は終わらないのか！？"
    
    show legioner_02
    
    シラン "良い質問ですが、私自身、最寄りの村まで歩いていくことが\n残っているかわからないので、あなたの力を節約してください。"
    
    player "理由はわかりませんが、茂みからのこれらの音は私を夢中にさせます。\n この場所は間違いなく呪われています。"
    
    シラン "ハハ、特にその年齢では、私は呪いを信じるほど迷信的ではありません。 注意すべきことがあれば、それは地元の略奪的な生き物か..."
    
    player "ああ、聞いた？?"
    
    シラン "ねえ、そのように私を怖がらせないでください、\n私たちはこの森に一人でいます。"
    
    player "しかし、私はそれが私たちの後に這っていたと確かに聞いた。" 
    
    シラン "おそらくそれは普通のヘビかトカゲでした。"
    
    player "普通のヘビにとって、この生き物は枝を大きく砕きすぎているように\n私には思えます。"
    
    シラン "さて、あなたがすべての悪魔を想像しているなら、\n茂みから行きましょう。 川の近くでは間違いなく落ち着くでしょう。"
    
    player "そうです、これらの森の音は私の心にはあまりにも悪いです。 \n川に沿って行く方がいいです。"
    
    scene river_bg with pushright
    pause(1.5)  # Wait 3 seconds after scene change
    
    player "ここはとても静かです。"
    
    show legioner_02
    
    シラン "そうです、今の主なことは水に落ちないことです、へへ。"
    
    player "ここはとても静かです。"
    
    hide legioner_02
    
    "数日間の行進が続き、森の中を進みます。"
    
    "彼らの目的地はローマ帝国のイベリアに\n位置する軍事基地「ルセントゥム」です。"
    
    "そこで、彼らは「セプティム・ゲミニ」（第7双子軍団）に配属され、\n次に「レギオ」（Legio）と呼ばれる都市に向かう予定です。"
    
    "イベリアの反乱軍がレギオを包囲し、彼らの到着が待たれています。"
    
    "この森の中ではさまざまな困難が待ち受けており、\n彼らの冒険はまだ始まったばかりです。"
    
    player "川で足を洗わなきゃ。この森の茂みから抜け出すのに、\n足の指が刺されまくってるよ。君もちょっと涼みたくないかい？"
    
    show legioner_02
    
    シラン "いいや、大丈夫だよ。重要なのは、食料が尽きたこと。キノコと\nベリー以外の食べ物が見当たらないんだ。僕はちょっと小獣を狩ってみるつもりだ。君は火を起こして、釣りでもしてみてくれ。"

    player "了解。ただ、森の中に深入りしないように。あの未知の生き物が\n君に襲いかかることだけは避けてほしいな。"

    シラン "また、君の森にまつわる妄想かよ。この森に怪物がいるわけないだろう、そんなの存在したら、僕が最初に感じるはずだ。まあ、僕が狩りに行ってくるよ。"

    "最初の軍団兵士は背を向けて、森に向かって歩き始め、手には投げ槍を握っていた。彼の仲間はただ頭を振り、足元の旅程のために履いた\nサンダルを脱ぎ、川に足を浸した。"
    
    hide legioner_02
    
    scene river_night_bg with pixellate
    
    "太陽は既に地平線の向こうに沈んでいた。"

    "川岸には小さなかがりびが燃えており、かがりびは茂みの端に集められた乾いた\n枝や草から点火されていた。"

    "最初の軍団兵士が去ってからすでに約3時間が経過し、\n彼の仲間は彼が狩りの間に迷子になっていないか心配し始めました。"

    player "あぁ、お前はいいやつだけど、自分から狩りに行くと言って、\nどこに行ったかすらわからなくなるのかよ。"

    "2番目の軍団兵士は、川に浸かりながらぼやきました。"

    player "見ての通り、彼は本当にここで道に迷ってしまうのかもしれない。\n備えあれば憂いなし、俺も彼の後を追って行かないといけないかもしれないな。"

    "危険な森の中に向かうことに恐れをなして、7番目の軍団兵士は\n深呼吸をし、立ち上がり、仲間の後を追うことを決意しました。"
    
    stop music
    scene forest_night_bg with fade
    play music forest
    
    player "くそ、暗いな。ここに来る前に少なくともたいまつを用意すれば\nよかった。"

    "軍団兵士の足元では、枯れた枝がパキパキと音を立て、\nその音ごとに彼の心臓が恐怖でバクバクと鼓動していました。"

    "恐怖を乗り越えるために、軍団兵士は自分につぶやきます。"

    "自分で呼んだわけだから、道を見失ったんじゃないかと心配している\n場合じゃない。"

    "彼は草むらを押しのけ、周りを見渡し、仲間を見つけようとします。"

    player "エイ、シラン！どこだ、この馬鹿野郎！お前、なんでこんなところに走り出すんだ！"

    "返答は無し。"
    
    $ renpy.music.set_volume(0.0)
    
    play sound heart
    
    "軍団兵士は立ち止まり、動けなくなりました。"

    "彼の足元には、彼の仲間シランが狩りに出かけるときに持ち出した\n槍が置かれていました。"

    "恐れることなく近づいて、槍を見つめます。"

    "ふむ、どうやら彼は背中から倒れて、這いずり回ろうとしたようだ…\nここには血の跡はないから、獣に襲われなかったみたいだな…でも、\nなぜ彼の足跡が襲撃の場所からたった数メートルのところで\n突然途切れているんだ？"

    $ background = change_background_with_sound_interrupt("forest_night_bg03") 
    with fade

    $ renpy.music.set_volume(1.0)
    
    "軍団兵は、シランという仲間を探し続け、暗い森をさまよっていました。暗い木々が四方から囲んでおり、深い夜はそれらの影をさらに不気味に\nしていました。葉の間からは自分の呼吸音と恐怖だけが聞こえました。"
    
    player "シラン！どこだ！"
    
    "私の足取りは慎重で、河岸の暗い輪郭に近づいて方向を見失わないように進みました。自分は不安定な状態で、内なる声はこの暗い森の中に一人ではいないと囁いていました。"
    
    "葉の間から奇妙なものを見つけました - 遠くで光る瞳、暗い低木の下から\n光り輝いていました。私は足を遅らせ、剣を抜き、可能な敵に備えました。"
    
    player "誰だ、そこにいるのか？シラン、君か？"
    
    "私の言葉は夜に消えてしまい、答えは分からない音と静かな囁きだけで、まるで何かが私に忍び寄っているかのようでした。私の決意は私を\n前進させ、暗闇の中に何が隠れているかを見極めようとしました。"
    
    "私はシランと最後に会った河岸のキャンプに戻ることに決めました。\n夜が進むにつれて、森はますます暗く、生き物のような謎めいた音と\n音を奏で、まるで中に浮かび上がる用意ができている秘密を秘めているかのようでした。"
    
    "森は暗く、無限の暗闇に沈んでいるかのようでした。私は前進し続け、\nシランの名前を叫びましたが、私の言葉は答えがなく、夜の中で凍りついていました。"
    
    scene forest_night_bg02 with fade
    
    player "シラン！どこだ！"
    
    "私の呼びかけに対する唯一の返事は、厚い沈黙でした。私の歩みと共に\n恐怖はますます近づき、まるで私をいつでも掴みかかる手が見えないかのようでした。"
    
    "私の目は、木々の間に囲まれている恐ろしい影に滑っていきました。私の\n内側は不確かさで満ち、この暗闇の中に一人ではいないという感覚を振り払うことができませんでした。"
    
    scene forest_night_bg04 with fade
    
    "そして、暗い低木の間から、遠くで光る瞳を見つけました。\nそれらは夜空を貫く2つの緑色の蛍光のようでした。"
    
    player "誰だ、そこにいるのか？シラン、君か？"
    
    "私の声は緊張から震えていましたが、答えはありませんでした。\n代わりに、音が大きくなり、何か隠れたものが私に近づいているかのようでした。"
    
    "私の手は剣を握り締め、どんな衝突にも備えていました。しかし、\n暗いシルエットは見えず、私は謎めいた遠くの蛍光の瞳に引き寄せられるように前進し続けました。"
    
    stop music
    
    play music wind
    
    show kuro_lamia_black3 at half_size_northeast with Dissolve(3.0)
    
    "そして、私には驚きでした。暗い木々の背後に、人間のシルエットが\n見えたのです。そのシルエットは凍てつく夜風を通り抜けているように\n動きませんでした。"
    
    player "おい、そこに誰かいるのか？シラン、君か、やっとか？"
    
    "私の声は緊張で充満していました。しかし、その姿はまだ静止し、\n何も言いませんでした。私は近づき、それがわなか敵かもしれないことを恐れました。私の心臓は耳で鳴っていて、その前にある暗い姿を見つめました。"
    
    hide kuro_lamia_black3
    
    show kuro_lamia_black2 at half_size_northeast2 with Dissolve(2.0)
    
    "徐々に輪郭がはっきりしてきて、私はその前に若い女性がいることに\n気づきました。彼女はオリーブ色のシャトーンに身を包んでいました。長くて黒い髪が肩に垂れ下がり、まるで夜の流れのようでした。彼女の目は深くて暗く、私の見えないものを見ているかのように静止していました。"
    
    player "大丈夫か？"

    "私の声は心配に満ちていましたが、彼女はまだ黙っていました。\n彼女は脅威ではないことを理解していましたが、この暗い森で彼女が存在することは不安を引き起こしました。"
    
    player "私は友達のシランを失いました。"
    
    "私は言いました、コンタクトを取ろうと努力しています。"
    
    player "私達はここでキャンプ場に向かう途中ですが、\n互いに迷子になりました。君は彼を見たことがありますか？"
    
    "女性はゆっくりと私に振り返り、彼女の目が私の目に合いました。\nそれらの目には空虚さだけでなく、私を強く引き付ける何かがあることを感じました。彼女は何か伝えようとしているようでしたが、言葉がありませんでした。"
    
    "完全な暗闇が私の足跡を隠し、私はまだこの謎の女性の視線を感じて\nいました。私のステップは遅くなり、森の音がますます静かになりました。そして、私の祈りに応えるかのように、月が厚い雲から徐々に現れ始めました。"
    
    hide kuro_lamia_black2
    stop music
    
    $ renpy.music.set_volume(1.0)
    play music terror01
    show kuro_lamia-transformed at camera_head_to_chest
    
    "女性は私の前に立っており、その姿は非常に神秘的で魅力的でした。\n月の光の下で、彼女の外見の各部分が特に表現豊かに見えました。"

    "長くて黒い髪は、夜の流れるような暗闇に光沢があり、\n特別な深みを与えているかのようでした。"

    "しかし、最も驚くべきことは、彼女の瞳が赤く輝いており、私に恐怖と\n喜びの混合物をもたらしていたことでした。その中には虚無感と何か不確かなものがあり、私の視線を引き寄せ、私を呆然とさせました。"

    "彼女の肌は青白く、完璧で、まるで大理石の像のようでした。\nそれは彼女の黒い髪と衣服と対照的でした。"
    
    show kuro_lamia-transformed at camera_chest_to_waist
    
    "月の光が私の周りを照らし、私の視線は私の心を凍りつかせる何かに落ちました。女性がシランの兜を手に持っていました。それは私の失われた仲間の兜であり、私の恐怖と希望が再び燃え上がりました。"
    
    "しかし、それ以上に驚くべきことが私には見えました。"
    
    "月の光の下で、彼女のシャトーンが明らかになり、その下から信じられないほどのものが伸びていることがわかりました。\n私は自分の目を疑いました。シャトーンからは巨大な蛇の尾がのぞき出ており、それは彼女の体の奥から生えているようでした。"
    
    "それは彼女の一部のようにそこにあって、月の光の下で大きな鱗がきらめいており、その尾は彼女の身長と同じほど長く、足の代わりにバランスを取っていました。それはまるで何の変哲もないことのようでした。"
    
    hide kuro_lamia-transformed
    
    show kuro_lamia:
        xalign 0.5
        yalign 0.5

    
    "私の考えは混乱し、心臓は激しく鼓動しました。これは、現実が私の目の前で崩れ去る瞬間でした。私は目の前にいる存在が何で、どのようにして存在できるのか理解できませんでした。私が生きてきた世界は崩壊し、\n私はこの奇妙で陰鬱な童話の中の小さな一部に過ぎなかったのです。"
    
    player "君は…君は何者だ？"
    
    "私の声は弦のように震えていました。"
    
    player "君はどうして…？"
    
    play sound hit
    stop music
    play music wind
    show blood:
        
    "突然、背後から何者かに襲われたような感覚が私を襲いました。私はふらりとなり、頭にぼんやりとした痛みが走りました。まるで鈍器で後頭部を打たれたようでした。"

    player "うぅ…"
    
    "私はかすかなうめき声を上げ、膝から崩れ落ちそうになりました。"
    
    scene forest_night_bg04_fall with fade
    hide kuro_lamia

    show kuro_lamia_fall:
        xalign 0.5
        yalign 0.3
    
    
    "その瞬間、意識がちらつき、視界がぼやけていきます。だんだんと周囲が暗くなり、最終的には真っ暗になってしまいました。"
    
    show forest_night_bg04_fall with dissolve
    show forest_night_bg04_fall_mask:
        alpha 0.00
        linear 5.0 alpha 0.5
        
    "その瞬間、私の意識がちらつき、視界がぼやけていきます。"
    
    # continuation of blackout
    show forest_night_bg04_fall_mask:
        linear 3.0 alpha 0.75
    
    "だんだんと周囲が暗くなり、最終的には真っ暗になってしまいました。私は混乱し、恐怖に支配されました。"
    
    # complete blackout
    show forest_night_bg04_fall_mask:
        linear 2.0 alpha 1.0
    
    "この奇妙な場所にいること、そして私が何者かに襲われたことについて考えました。また、私の友人であるシランの安全も心配しました。"

    "この暗闇の中で、私は何が起こるのかを全く知らないまま、ただ身を任せざるを得ませんでした。"
    
    "{color=#FF0000}ゲームのデモバージョンのテストに参加していただき、ありがとうございます！お客様のご協力とフィードバックは非常に重要です。何かご意見、ご要望、またはフィードバックがある場合は、どうぞお気軽にお知らせください。{/color}"

    "{color=#FF0000}ゲームのデモバージョンと当プロジェクトの開発の最新情報については、GitHubのプロフィールでご確認いただけます：{a=https://github.com/Ruslan-dev-Free-Fire}Ruslan-dev-Free-Fire{/a}。{/color}"

    "{color=#FF0000}お客様のご支援に感謝申し上げます！お楽しみいただけたら幸いですし、今後もご意見や提案をお待ちしております。{/color}"

