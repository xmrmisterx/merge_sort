# merge_sort

Alright, so this is another sorting algorithm, using recursion this time. Apparently one of the benefits of merge sort, vs something like bubble sort, is that bubble sort can take n squared time, whereas merge sort is big O times n log n; basically uses less memory.

Ok, so we got the base condition from the explanatory videos on merge sort, that being when the number of elements in the array is less than 2 (or less than or equal to 1). Are we returning something when this condition is met? The videos didn't say, so for now we'll assume we aren't returning anything, but the previous recursive exercises usually returned something when the base condition is met. Now, there were 3 main steps of pseudocode explained: 1) Sort the left side 2) Sort the right side 3) Merge the two sides.

Alright, so let's get coding. We know we want a parameter for at least the initial array, and we'll need to return a sorted array, so there's probably the final array that we'll want to carry around as a parameter as we add to it, maybe. Let's start coding. Hmm... so we're at our base condition, when the array is at length 1 or less, but what do we do here? Honestly I'm not sure, so let's leave that part of the code for now. We'll know more when we actually create the body of the code, as to what to do when it gets to sortable size.

Ok, so we're gonna break the array into halves but... how do we even do that? I don't think i've ever tried to split an array or string in half before. Apparently there is a "split" method for arrays, but we're not sure what it does bc the ruby docs seem kind of bare. Let's test it in terminal. Lol, what, we get an error saying split is an undefined method, that's nice. It's looking like there's no inbuilt method for this. However, googling got us thinking. We know that splitting something means dividing it in half. And from our school coding on odd and even numbers, we feel like we can use arr.length and the "%" operator to determine if an array will divide evenly, and if it doesn't, we can round down the quotient and add one to that to get the mid way point. Actually, if it's not an even number of elements, meaning we can't divide it evenly, it doesn't matter, we still divide it, we just need to determine what we want to with the non even remainder, round up or round down. Then, we'll want to actually cut up the array. Now, this is either from calling a range for the arr with the ranges defined by where is the halfpoint, or using something like "slice" and once again cutting off the portions that we want. Alright, let's code this and test this part.

Hmm... it seems like there are actually 2 different ways to need to split an array. If it's even, the first and second halves are "arr2 = arr1[0..(arr1.length/2)-1], arr3 = arr1[(arr1.length/2)..arr1.length]", but if it's odd... Actually testing in terminal reveals this is fine for both. This will place the smaller pair on the left, and the bigger pair on the right if the array is uneven, and will split it evenly if the arrays are even, so we don't need separate code sections for odd and even, which makes it alot cleaner.

Alright, so it seems that we're gonna get a bunch of 1 element arrays from recursively calling this function, but how do we compare one array to another? I think maybe thinking it in terms of left and right array is throwing us off. What if we just consider it as a recursive function. Where and how do we want to call the function again, and how do we actually sort all these 1 element arrays?

We took like a two week break and now coming back to this... We rewatched the first video on merge sort, and honestly it's still murky. I think the key is how do we sort arrays and where are all these arrays being created and contained... The first thing we noticed was our check to see if the arr length is 1 or less, which is currently at the beginning, but that doesn't make sense to us. We are starting big, and going smaller, so shouldn't the code for the bigger initial arrays be on top? I think this makes sense, so let's change that.

Alright, so currently our function takes the initial array, and breaks it in half, then calls merge sort on the left and right halves of those. Now, what this does is inevitably we'll have a bunch of 1 element arrays. The question is, how do we compare one array to another to see which one is bigger? After that, where do we put the new sorted array?

We went and watched the 3rd video in the assignment (each video gives more hints than the previous video). This one actually gave the psuedocode, and it kindas makes sense. It says that we have to put the left side of the original array into another array (i.e. left arr) and the right side into another array (i.e. right arr), then merge them together at the end. This is a little helpful because we weren't thinking about making new copies of arrays.

Ok, so playing around with array functions, "slice!" is the function we want, the destructive version with the "!" to modify the old array. It's funny having to relearn some of these functions after a couple of weeks. Ok, so we'll use this method when we want to start modifying arrays and creating new ones.

Ok, so thinking about this recursive function. It seems it's gonna call on the arrays, and keep splitting them, which eventually leads to the recursive function calling itself with an arr with either 1 or 2 elements. If it's 2 elements, we want to compare the first and second element and sort them in smallest to biggest order and put them into a new array. If it's one element, it's already sorted, but we're gonna have to put that in a temporary array so that it can be sorted vs the 2 element array, after that has been sorted. The importance of all of this is that, there are certain array lengths where we want to start sorting and then merging.

At length 1, we want to keep in some temporary array for future comparison, bc it's already sorted. At length 2, we can stop calling merge sort recursively, and sort between element 0 and element 1, then put the 2 ordered items into another temporary array.

Once we have all the sorted arrays, how do we merge them? Where are arrays to be merged coming from? Ok, we did some test runs with our code for comparing arrays, then placing them into a new array and returning that array. The video said once one of the two comparison arrays has been depleted, just to add the other one to the final array because it's already sorted. However, it adds the array within an array, so we had to flatten the array out to make it look proper. One thing we noticed, is that the arrays aren't sorted in order in our test function. Without calling recursively, all the arrays are not sorted. So we have to think, what is the recursion doing that is sorting the arrays? How do we code it to sort? Because the cs50 video made it sound simple. We just compare the first 2 elements of our 2 arrays, and the smaller one gets put into a new sorted array. However, this doesn't work if the arrays of the 2 aren't sorted first. So, are we doing that with our code?

Ok, so we finish our function and go to test it, and we're getting an undefined method "length" for nil class. We think the code is not working bc we put, inside our if statement asking if arr.length == 1, if arr length < 1, and maybe that's what's causing problems. Another thing could be our destructive slice function is causing problems? Our debug shows that its getting to the "arr length==1" part of the code, but that's where we're getting the rejection.

Ok, we put a puts at this line, outputting the left and right arrays. Maybe there is no array left, to call the length function on the arrays? Bc we know that length is definitely an array method. Run this again tomorrow and test that. Looking over the outputs, it seems like when the code gets the array to one element, then it puts out that array, it doesn't puts out anything, like the arr is empty, but why is the array empty if it has 1 element lol. Looking more at the code, we see what's going on now. We are whittling down our array using recursion, until there is 1 element left, but then we try to call the length methods on the left and right arrays, but they aren't there? I'm not sure where they exist in the code but... when the whole arr is at 1 element, you can't really have a left and right array.

Ok, so we decide to change the parameters. Now instead of array length being equal to 1 wen we sort, it's equal to 2, and we split the arrays before sorting. When are recursively calling the function when array length is 3 elements long or longer now, instead of 2 elements long like before. This next iteration is better, it did add some elements to the new array. However, the right array got broken down from a 3 element to a 1 and 2 element, and I think the 1 element arr broke our code, bc now we don't have a condition for what to do with the 1 element arrays.

I dont think we want to change a couple of things here. First off, there's no condition for 1 element arrays, so we need to add a condition, which probably means adding it to some temporary array. Secondly, I think we want more than just the original array as a parameter.  I think we should have a second and third optional parameters called left and right arr, so that when things are broken down into 1 element arrays, we can access the left and right arrays to starting putting back together.

Watching more of the last video, there's another way to increment through each element that doesn't involve destruction of the array. I'm pretty sure destroying the array is gonna cause problems, so we should probably look into coding it without the destructive method.

Alright, so we finally finished watching the third video, and the diagram is pretty simple. We will keep recursively calling this function, until there are only 1 element arrays left. At this point, we will starting merging them, but before that, we have to consider this. How do we access all the 1 element arrays to compare with each other? Are they gonna be stored in a parameter passed to the function? Furthermore, the diagram starts off with an array with even number of digits, which means they all split evenly, but what happens when there are odd number of elements, how do we split a 3 element subarray and store the 1 element array to be later used to compare with? These are the questions we have to answer to fully understand what we want the code to do.

Let's consider the first issue. If we have an odd number of elements, where do we store the 1 element arrays while working on the 2 element+ subarrays. Actually I think it's best to consider the case where there is an even number of arrays. Let's make it work in an easier setting first, then alter fit to fit the harder circumstances. Alright, so we assume the array starts off evenly and breaks into evenly divided chunks, so eventually the arrays all break down into 1 element arrays. How do we even compare the 1 element arrays afterwards?

***Can't every iteration of the array carry over the left and right sides as some formula from the original array? I like this idea. Each time we recursively call, we have the right and left sides as parameters. Then when the array becomes one element, what exactly do we do with the left and right sides, that doesn't do anything lol. It seems like we have to start comparing them when they are at 2 elements, not 1 element. When the array finally gets down to 2 elements, we can break it into two, then compare the left and right sides. That seems pretty easy. This isn't like any of the videos lol, which say to break it down to 1 element arrays, so hopefully we can make it work.***

So, let's assume that we can break it down into 2 element arrays and compare the halves... Then what? We'll need to start combining the arrays now... So, we have the left and right side of the 2 element arrays, which we compare, then put that into some temporary array. This also needs to called recursively to glue together all the smaller arrays? Or does the function naturally put them together? If it's recursive, how do we call the function and make it keep merging the progressively bigger arrays, as opposed to these arrays triggering the length requirements for breaking down into smaller arrays? If we still have the size of the broken down arrays as a parameter, then it shouldn't trigger the further breaking down part? It seems we'd need 4 parameters: arr1, left_arr, right_arr, final_array.

Let's go over this again conceptually and see if it makes sense. Our function starts off with just accepting the first parameter arr1, and left_arr, right_arr, and final_array are set to their default values of [], or a blank array. We go to the conditional statement that checks if the array is bigger than 2 elements, and it is, at which point we split the array into a left_arr and a right_arr. Each of these arrays will call the function again, but this time, we add a left and right arr parameter, while still leaving the final array blank [When we call the function for the first time recursively, what is arr1, left_arr, and right_arr? I think arr1 should be the whole current left or right arr, then left_arr and right_arr are the split of versions of that]. Eventually the recursive calls should stop when we get arr1 to 2 elements, at which point, we get to our first comparison. So, we'll compare the left_arr vs the right_arr, see which is smaller, put the smaller one into the final array first, then the larger one into the final array. Now what? Do we call the function recursively again, and put in the final array as a parameter finally? What is the current final_array that we put inside the parameter gonna be compared with?

Yeah, this seems complicated. How do we actually do the merging in merge sort? Hmmm.. so after our workout we had an idea. Isn't this alot simpler if we condense everything into a simple function? All of this is done in one function, and we remembered the steps from the last video. Can we make it as simple as copying the original array into a left and right array, then after we have merged down to 1 element arrays, just combining the left and right arrays into a final array? Let's go over the pseudocode again...

So we call the function for the first time, and there is only 1 parameter, the array we want to sort. Then we do a check for array length. If it's greater than 2, we want to split into left and right array. [What if it's 2? What do we do? Now that we think about it, I think we do want to break everything down into 1 element, but there will be multiple checks] So yeah, there will be multiple checks. We first check the original array, and if greater than 2 elements, we will break it into left and right array. So this will keep running until we get to 2 element arrays. Then what do we do? If there are 2 elements, we will break it up into 1 element arrays. Then what? I think at this point, we don't want to split anymore, bc they are already split,and the pair is here to compare, we don't want to recur the function here, or we will lose reference to each pair.

So at this point, we're at the comparison stage. This is after all the breaking down into smaller subarrays. At this point, we'll have a left and right array, which we'll compare and the smaller one goes into a final array, or maybe 3rd array, or sorted array, whatever, the name doesn't really matter. So what do we do with this sorted array? This is the array that we return. I think this is the problem that we weren't able to solve. We aren't really carrying around any left and right arrays, and we aren't accumulating the final array from pair after pair. Basically we run the whole function, on the array. Let's repeat it back and see if it makes sense. We break down an array, into at least 2 element blocks. Then we break it down again, but now we have 2 halves, and we compare those halves to see which is smaller and put them into a sorted array in order, then we return this array. When this gets run recursively, the 2 element arrays will be 4 element arrays, which will be 8 element arrays, and we return the final sorted array. There is no other parameter besides the array to be sorted. Let's actually migrate this to Python code as well...

We need to figure out how to copy all the text from our virtual machine onto here, as we have alot of info there that we want to transfer over to this Python Pycharm program. We ended up having to send that info to our email address on the virtual machine, then open up our email and copy and paste it onto here. Not convenient, but it worked.

As for the current code, we need to convert the splitting of list code from our Ruby code into Python, and flesh out all the pseudocode we've used. 

After a night of sleep, we had some extra ideas. So I think we actually want to take it down to 1 element arrays. Before, we weren't sure what to do with the one element arrays. Like, do we store them in the parameter or what? But after thinking about it, the solution is to probably return the function with an sorted array of 1 element, just as we would after all the merging is done and end up with a final sorted array. Alright, let's go back and change our pseudocode a bit before putting in the code to fill out the pseudocode. 

Wow, this breaking down of the list into 2 halves took alot longer than we thought lol. Python doesn't use ranges for lists, but slices, which we knew about, but didn't really realize until our ranges didn't work, we had to use slice ranges. Also, when we divided the lists in half, we got floats, which doesn't work in a range (and probably not in slices either, but we fixed the range issue before getting to slices), so we had to cast the divided values as integers. Thirdly, ruby ranges were inclusive, but python ranges exclusive, so we had to remove the -1 factors that we put into the ranges to get them to split in half. With that said, it looks like the code is fine now, so we've successfully divided our list in half now.

We incorporate our sorting code for the left and right lists after they are done recurring, put in a print at every step to make sure we are getting the results we want from our code, and surprisingly we didn't get an error. It compiled and ran first try, and look at the print outputs, all the values were what we wanted them to be, so obviously that's very good. Now, we need to code the part where one of the list halves is gone. In this case, we want to check to see which half is missing, and add the rest of the other half (since it should all be sorted already) into our sorted array, then return our sorted array.

So that code was pretty small and it worked, we got the full list back. However, the remaining part of the list half appended into our sorted array (this should be called sorted list lol) as a list itself, so now we have a list within a list, which we obviously don't want. We Google for python "flatten" function, but it doesn't seem like there is one. We're gonna have to write quite a bit of code to flatten this out. With that said, I think we already know how to fix this. Just iterate through the list half, and append each item to our sorted array. This should eliminate it all coming in at once as a list.

Alright, so that did work. We forgot how to do a for loop with a range, it's a little different than in Ruby, but we figured it out. Now, I think this code is done. We're gonna have to run the whole thing and see what happens, but conceptually I think we have all of the elements of this merge sort algorithm. Let's run it with a test list and see what we get. I'd probably start with an even list lol. Interesting, so the algo seems to be sorting some things, but not everything. Can we put more print statements in and see exactly what's going on? The recursion makes it very hard to keep track of everything.

After looking at our prints outputs, we see that, although we tested the code and it works fine, we weren't testing the recursion. When recursion happens, the arrays that get sorted are getting mixed up. Following the left half [6,8,3] we see that it gets broken down into 6 and 8,3, which is correct. Then 6 gets returned,and 8,3 is broken down into 8 and 3, which is correct. So, now we have 6, 8, and 3, all returned and all single element lists. It does 8 and 3 lists first, which is also correct, we want that to go before comparing this list with the 6 list. The sorting of 3 and 8 works, and the sorted array becomes [3,8]. Now, it tries to sort 6 and 8, but this is incorrect. It should be trying to sort 6 and 3,8. I think maybe the destruction of the arrays is causing problems with the remaining arrays? It's possible. Let's change our code so that we don't destroy the elements after adding them to sorted array.

So, currently the code has a while loop, which checks for both list lengths, and if they are greater than 0 (there is at least 1 element in them), they will continue to sort. We destroy the elements of the list as they are added to the sorted array so that eventually the while loop breaks. If we don't destroy the elements, how are we keep tracking of when we reached the end of a list for sorting purposes? The third video in the assignment says we have to assign a pointer to each array (maybe a counter?) and if that counter passes the number of elements in the array, then it stops. I guess that can be our stop condition. What does that mean for the rest of our code? How do we append the correct element to the sorted array. This should be the index of that list, which corresponds to the value of the counter. Alright, let's try to code this and test in out separately before putting inside the recursive function.

Lol, we finally get the code to sort without destroying the elements. Took a while to write, but, we get the same wrongly sorted list at the end, with the 3 at the very end. Check the print logs and go step by step, to see what the code is doing wrong. It's still getting caught in that same area, where after the first 6 and 8,3 pair, it goes to do the 6 and 8, so it seems the first merge of the 1 elements are working correctly, but why isn't the second merge working? If we have a left list of 6,8,3, then 8 and 3 gets compared first, we get 3,8, then 6 should compare with that 3,8, but it's comparing to 8, not even sure where that 8 is coming from. Let's try putting the sorted array as a default parameter in our function, then return it at the end of the function and see what happens? After that, let's try a simpler array, like 4 elements to see the logic better. Yeah, I think we see now that when they are single elements they merge fine, but the second round of merging, is not using the sorted arrays for merging, but lists that i'm not sure where they are coming from.

Ok, so it looks like after we sort the single element lists with our initial list of [9,3,4,1] we get 3,9 and 1,4 for,which is correct. But in the next round of merging, instead of comparing 3,9 and 1,4, it compares 9,3 and 4,1, which appear to be the initial values of the left and right list. How do we update the new values of each list half to be compared? We're not exactly sure how to carry over the sorted array so that it gets compared. Let's look over the third video and see the pseudocode they used again. If not, we're gonna have to look at some merge sort algos in Google. What if we save our sorted array as list1 and return the list1, does that do anything? Lol, that didn't do anything. I mean, we've set the left and right lists of the original list equal to certain lists, then called merge sort on them. These lists will not change right? So how do we end up comparing 2 sorted lists? It sounds like a parameter needs to be passed, but we're not sure how to pass the sorted arrays.

Googling, it shows that in one implementation, the original list gets destroyed. The original list is the sorted array! Is this the breakthrough that we needed? If we change the original list along the way, does that update the "sorted array" that we've been using? Let's try it out. Actually, currently our code sorts the 2 list halves, then appends that element onto a blank "sorted array". If we want to replace the original list as we go on, how do we do that? We need to set the list index to a variable and increment it, so that we start with 0, and go all the way to our list length.

Wow, that was actually the secret sauce that finished our code. The "sorted array" we kept trying to add sorted elements to and pass on to the next cycle of merging, was actually the original array. By changing the original list with the sorted elements, we were able to update the left and right lists without having to pass through another sorted list as some parameter. The only change we needed to make to our code was to add another variable to keep track of what element in the original list needed to be updated.

I really like this Pycharm using Python compared to using terminal and Ruby. It seems to compile alot faster and has some extra features that could be useful. We remember having to wait like 1 hr+ to compile our tic tac toe game on terminal lol. We want to comment out this code, and upload it to our other github. How do we do that, since this one is linked to our school github.

This is a copy of our code after finishing, with the prints for debugging purposes.

def merge_sort(list1):
    if len(list1) < 2:

        return list1

    else:  # if list has 2 elements or greater...

        # print("list is >= 2, len(list1):", len(list1))

        left_list = list1[0:int(len(list1)/2)]
        right_list = list1[int(len(list1)/2):len(list1)]
        # print("left list:", left_list, " right list:", right_list)

        merge_sort(left_list)
        merge_sort(right_list)

        sorted_list_counter = 0
        left_list_counter = 0
        right_list_counter = 0
        while (len(left_list) > left_list_counter) & (len(right_list) > right_list_counter):
            # print("left list:", left_list, "len(left_list):", len(left_list), " left list counter:", left_list_counter,
            #     "right list:", right_list, "right list length:", len(right_list), " right list counter:", right_list_counter)
            if left_list[left_list_counter] < right_list[right_list_counter]:
                # print("left_list[left_list_counter]:", left_list[left_list_counter], " < right_list[right_list_counter]:",
                #     right_list[right_list_counter])
                list1[sorted_list_counter] = left_list[left_list_counter]
                sorted_list_counter += 1
                # print("sorted list now:", list1, " with sorted list counter:", sorted_list_counter)
                left_list_counter += 1
                # print("left_list_counter now:", left_list_counter)
            else:
                # print("left_list[left_list_counter]:", left_list[left_list_counter], " >= right_list[right_list_counter]:",
                #     right_list[right_list_counter])
                list1[sorted_list_counter] = right_list[right_list_counter]
                sorted_list_counter += 1
                # print("sorted list now:", list1, " with sorted list counter:", sorted_list_counter)
                right_list_counter += 1
                # print("right_list_counter now:", right_list_counter)

        if len(left_list) == left_list_counter:
            # print("len(left_list) == left_list_counter")
            for val in range(right_list_counter, len(right_list)):
                list1[sorted_list_counter] = right_list[val]
                sorted_list_counter += 1
                # print("sorted list now:", list1, " with sorted list counter:", sorted_list_counter)
        elif len(right_list) == right_list_counter:
            # print("len(right_list) == right_list_counter")
            for val in range(left_list_counter, len(left_list)):
                list1[sorted_list_counter] = left_list[val]
                sorted_list_counter += 1
                # print("sorted list now:", list1, " with sorted list counter:", sorted_list_counter)


    # print(list1)
    return list1


# list1 = [6,8,3,2,4,7]
# list1 = [9,3,4,1]
# list1 = [5,2,4,7,9]
# merge_sort(list1)