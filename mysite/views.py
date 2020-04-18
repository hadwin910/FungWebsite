from django.shortcuts import render

from .models import Contact
from .models import Titanic
from . import ml_predict
import random


def index(request):
    return render(request, 'mysite/index.html')


def about(request):
    return render(request, 'mysite/about.html')


def onwork(request):
    return render(request, 'mysite/onwork.html')


def portfolio(request):
    return render(request, 'mysite/portfolio.html')


def contact(request):
    if request.method == "POST":
        email_r = request.POST.get("email")
        subject_r = request.POST.get("subject")
        message_r = request.POST.get("message")
        c = Contact(email=email_r, subject=subject_r, message=message_r)
        c.save()
        m1sent = "Your message is sent!"
        context = {'messagesent': m1sent}
        return render(request, 'mysite/contact.html', context)
    else:
        return render(request, 'mysite/contact.html')


def mlmodel(request):
    if request.method == "POST":
        pclass_r = request.POST.get("pclass")
        sex_r = request.POST.get("sex")
        age_r = request.POST.get("age")
        sibsp_r = request.POST.get("sibsp")
        parch_r = request.POST.get("parch")
        fare_r = request.POST.get("fare")
        embarked_r = request.POST.get("embarked")
        title_r = request.POST.get("title")
        s = ml_predict.prediction_model(pclass_r, sex_r, age_r, sibsp_r, parch_r, fare_r, embarked_r, title_r)
        c = Titanic(survived=s, pclass=pclass_r, sex=sex_r, age=age_r, sibsp=sibsp_r, parch=parch_r, fare=fare_r,
                    embarked=embarked_r, title=title_r)
        c.save()
        surdic = {1: 'survive', 0: 'decease'}
        gets = surdic.get(int(s))
        pcldic = {'1': '1st class', '2': '2nd class', '3': '3rd class'}
        sexdic = {'0': 'male', '1': 'female'}
        embdic = {'0': 'Southampton', '1': 'Cherbourg', '2': 'Queenstown'}
        titdic = {'0': 'Mr', '1': 'Miss', '2': 'Mrs', '3': 'Master', '4': 'Dr', '5': 'Rev', '6': 'Officer', '7': 'Royalty'}
        restr = "The " + str(age_r) + "-year-old " + sexdic[sex_r] + " person with a title of " + titdic[title_r] + " in the " + pcldic[pclass_r] + " with a fare of " + str(fare_r) + " with " + str(sibsp_r) + " siblings/spouses and " + str(parch_r) + " parents/children, embarked from " + embdic[embarked_r] + ", is predicted to "+ gets + "."
        m1sent = restr
        '''if s==1:
            m1sent="This person is predicted to survive."
        elif s==0:
            m1sent = "This person is predicted to decease."
        else:
            m1sent = "The prediction has encountered error."'''
        context = {'survival': m1sent}
        return render(request, 'mysite/mlmodel.html', context)
    else:
        return render(request, 'mysite/mlmodel.html')


def philosophy(request):
    quotes = [
        "I have often enough asked myself, whether on the whole philosophy hitherto has not generally been merely an interpretation of the body, and a misunderstanding of the body. Nietzsche",
        "I think I am justified in characterizing the four elements as the hormones of the imagination.   ~Bachelard",
        "Lovers are like 'two mirrors facing one another where two indefinite series of images set in one another arise which belong really to neither of the two surfaces, since each is only the rejoinder of the other, and which therefore form a couple, a couple more real than either of them'.   ~Merleau-Ponty",
        "But the life of man is of no greater importance to the universe than that of an oyster.  ~Hume",
        "The thing is to find a truth which is true for me, to find the idea for which I can live and die.   ~Kierkegaard",
        "When I begin to ‘write’, I do not write, I snuggle up, I become an ear, I follow a rhythm.    ~Cixous",
        "The history of the world is none other than the progress of the consciousness of freedom.    ~Hegel",
        "He who cannot lie does not know what the truth is.   ~Nietzsche",
        "All things are subject to interpretation whichever interpretation prevails at a given time is a function of power and not truth.   ~Nietzsche",
        "Life has no meaning the moment you lose the illusion of being eternal.   ~Sartre",
        "There is an old illusion-it is called good and evil.   ~Nietzsche",
        "That which needs to be proved cannot be worth much.   ~Nietzsche",
        "Anything, anything would be better than this agony of mind, this creeping pain that gnaws and fumbles and caresses one and never hurts quite enough.   ~Sartre",
        "To make the individual uncomfortable, that is my task.   ~Nietzsche", "Hell is other people.   ~Sartre",
        "The thought of suicide is a powerful solace: by means of it one gets through many a bad night.   ~Nietzsche",
        "Art is the proper task of life.   ~Nietzsche",
        "Change your life today. Don't gamble on the future, act now, without delay.   ~Beauvoir",
        "One's life has value so long as one attributes value to the life of others, by means of love, friendship, indignation and compassion.   ~Beauvoir",
        "One is not born a woman, but becomes one.   ~Beauvoir",
        "I wish that every human life might be pure transparent freedom.   ~Beauvoir",
        "When an individual is kept in a situation of inferiority, the fact is that he does become inferior.   ~Beauvoir",
        "Society cares for the individual only so far as he is profitable.   ~Beauvoir",
        "It is not in giving life but in risking life that man is raised above the animal; that is why superiority has been accorded in humanity not to the sex that brings forth but to that which kills.   ~Beauvoir",
        "To catch a husband is an art; to hold him is a job.   ~Beauvoir",
        "I tore myself away from the safe comfort of certainties through my love for truth - and truth rewarded me.   ~Beauvoir",
        "If you live long enough, you'll see that every victory turns into a defeat.   ~Beauvoir",
        "Art is an attempt to integrate evil.   ~Beauvoir",
        "One is not born, but rather becomes, a woman.   ~Beauvoir.",
        "It is old age, rather than death, that is to be contrasted with life. Old age is life's parody, whereas death transforms life into a destiny: in a way it preserves it by giving it the absolute dimension. Death does away with time.   ~Beauvoir",
        "Two things awe me most, the starry sky above me and the moral law within me.   ~Kant",
        "In law a man is guilty when he violates the rights of others. In ethics he is guilty if he only thinks of doing so.   ~Kant",
        "Science is organized knowledge. Wisdom is organized life.   ~Kant",
        "Always recognize that human individuals are ends, and do not use them as means to your end.   ~Kant",
        "All our knowledge begins with the senses, proceeds then to the understanding, and ends with reason. There is nothing higher than reason.   ~Kant",
        "Metaphysics is a dark ocean without shores or lighthouse, strewn with many a philosophic wreck.   ~Kant",
        "Genuine tragedies in the world are not conflicts between right and wrong. They are conflicts between two rights.   ~Kant",
        "Nothing great in the world has ever been accomplished without passion.   ~Kant",
        "Education is the art of making man ethical.   ~Kant", "World history is a court of judgment.   ~Kant",
        "Mark this well, you proud men of action! you are, after all, nothing but unconscious instruments of the men of thought.   ~Kant",
        "An idea is always a generalization, and generalization is a property of thinking. To generalize means to think.   ~Kant",
        "...more than other senses, the eye objectifies and masters. it sets at a distance, maintains the distance. in our culture, the predominance of the look over smell, taste, touch, hearing, has brought about an improverishment of bodily relations...the moment domin ates the look dominates, the body loses its materiality.   ~Irigaray",
        "Sexual difference is probably the issue in our time which could be our 'salvation' if we thought it through.   ~Irigaray",
        "Between gods and men, territories are set up. At least in the no-man’s land of the heights of heaven, the depths of hell, and inside the boundary traced by the oceans. Dimensions installed by a cosmogonic trilogy that leaves each term in its generic place. There remains the earth ancestress, a fourth term, that was once the most fertile, that has been progressively buried and forgotten beneath the architectonic of patriarchal sovereignty. And this murder erupts in the form of ambivalences that have constantly to be solved and hierarchized, in twinned pairs of more or less good doubles.   ~Irigaray",
        "Censor the body and you censor breath and speech at the same time. Write yourself. Your body must be heard.   ~Cixous",
        "You only have to look at the Medusa straight on to see her. And she's not deadly. She's beautiful and she's laughing.   ~Cixous",
        "People know what they do; frequently they know why they do what they do; but what they don't know is what what they do does.   ~Foucault",
        "Where there is power, there is resistance.   ~Foucault",
        "Knowledge is not for knowing: knowledge is for cutting.   ~Foucault",
        "...if you are not like everybody else, then you are abnormal, if you are abnormal , then you are sick. These three categories, not being like everybody else, not being normal and being sick are in fact very different but have been reduced to the same thing.   ~Foucault",
        "I'm no prophet. My job is making windows where there were once walls.   ~Foucualt",
        "The real political task in a society such as ours is to criticize the workings of institutions that appear to be both neutral and independent, to criticize and attack them in such a manner that the political violence that has always exercised itself obscurely through them will be unmasked, so that one can fight against them.   ~Foucault",
        "Maybe the target nowadays is not to discover what we are but to refuse what we are.   ~Foucualt",
        "But the guilty person is only one of the targets of punishment. For punishment is directed above all at others, at all the potentially guilty.   ~Foucualt",
        "The intellectual was rejected and persecuted at the precise moment when the facts became incontrovertible, when it was forbidden to say that the emperor had no clothes.   ~Foucualt",
        "The 'Enlightenment', which discovered the liberties, also invented the disciplines.   ~Foucualt",
        "What desire can be contrary to nature since it was given to man by nature itself?   ~Foucault",
        "You may have killed God beneath the weight of all that you have said; but don't imagine that, with all that you are saying, you will make a man that will live longer than he.    ~Foucault",
        "The art of living is more like wrestling than dancing. ~Marcus Aurelius",
        "You forget that the fruits belong to all and that the land belongs to no one. ~Rousseau",
        "Necessity is blind until it becomes conscious. Freedom is the consciousness of necessity. ~Marx",
        "The higher we are placed, the more humbly we should walk. ~Cicero",
        "Out of life's school of war: What does not destroy me, makes me stronger. ~Nietzsche",
        "What difference does it make how much you have? What you do not have amounts to much more. ~Seneca",
        "Freedom is absolutely necessary for the progress in science and the liberal arts. ~Spinoza",
        "Words are more treacherous and powerful than we think. ~Sartre",
        "Misfortune shows those who are not really friends. ~Aristotle",
        "Men's ideas are the most direct emanations of their material state. ~Marx",
        "Being is. Being is in-itself. Being is what it is. ~Sartre",
        "The motive power of democracy is love ~Henri Bergson",
        "Governments have never learned anything from history, or acted on principles deducted from it. ~Hegel",
        " Every parting gives a foretaste of death, every reunion a hint of the resurrection. ~Schopenhauer",
        "Amid the pressure of great events, a general principle gives no help. ~Hegel",
        "Talent hits a target no one else can hit; Genius hits a target no one else can see. ~Schopenhauer",
        "Time passes irrevocably. ~Virgil", "Death is not the worst that can happen to men. ~Plato",
        "Insanity in individuals is something rare - but in groups, parties, nations and epochs, it is the rule. ~Nietzsche",
        " I don't know why we are here, but I'm pretty sure that it is not in order to enjoy ourselves. ~Wittgenstein",
        "The only antidote to mental suffering is physical pain. ~Marx",
        "The young are permanently in a state resembling intoxication. ~Aristotle",
        "Social progress can be measured by the social position of the female sex. ~Marx",
        "Like all dreamers, I mistook disenchantment for truth. ~Sartre",
        "The eye sees only what the mind is prepared to comprehend. ~Henri Bergson",
        "Take the course opposite to custom and you will almost always do well. ~Rousseau",
        "Beauty is no quality in things themselves. It exists merely in the mind which contemplates them. ~Hume",
        "Generally speaking, the errors in religion are dangerous; those in philosophy only ridiculous. ~Hume",
        "What worries you, masters you. ~Locke",
        "If people never did silly things nothing intelligent would ever get done. ~Wittgenstein",
        "Man is born free, and everywhere he is in shackles. ~Rousseau",
        "Someone who knows too much finds it hard not to lie. ~Wittgenstein",
        "Freedom is what you do with what's been done to you. ~Sartre",
        "Life begins on the other side of despair. ~Sartre",
        "The endeavor to understand is the first and only basis of virtue. ~Spinoza",
        "If man makes himself a worm he must not complain when he is trodden on. ~Kant",
        "From the first day to this, sheer greed was the driving spirit of civilization. ~Engels",
        "I have always said and felt that true enjoyment can not be described. ~Rousseau",
        "World history is a court of judgment. ~Hegel",
        "This is really cool! An animated tour of the invisible http://on.ted.com/LloydAnimated",
        "The human body is essentially something other than an animal organism. ~Heidegger",
        "If I take death into my life, acknowledge it, and face it squarely, I will free myself from the anxiety of death and the pettiness of life - and only then will I be free to become myself. ~Heidegger",
        "The possible ranks higher than the actual.  ~Heidegger",
        "The human being is not the lord of beings, but the shepherd of Being. ~Heidegger",
        "The most thought-provoking thing in our thought-provoking time is that we are still not thinking. ~Heidegger",
        "Why are there beings at all, instead of Nothing? ~Heidegger",
        "Thinking begins only when we have come to know that reason, glorified for centuries, is the stiff-necked adversary of thought. ~Heidegger",
        "Man acts as though he were the shaper and master of language, while in fact language remains the master of man. ~Heidegger",
        "Only a god can save us. ~Heidegger",
        "Language is the house of the truth of Being. ~Heidegger",
        "And the Other whose presence is discreetly an absence, with which is accomplished the primary hospitable welcome which describes the field of intimacy, is the Woman. ~Levinas",
        "To write poetry after Auschwitz is barbaric. ~Adorno",
        "Truth (discoveredness) must always first be wrested from beings. ~Heidegger (Being and Time paragraph section44)"]
    num = int(random.random() * (len(quotes) - 1))
    texy = quotes[num]
    context = {'Text1': texy}
    return render(request, 'mysite/philosophy.html', context)

# Create your views here.
