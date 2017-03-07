
data Bst a = Nil | Node (Bst a) a (Bst a)
  deriving (Show)

bstWalk :: (Show a, Ord a) => Bst a -> IO ()
bstWalk Nil = putStrLn ""
bstWalk node = putStrLn $ showHelp node
  where 
    showHelp Nil = " nil "
    showHelp (Node l v r) = show (v) ++ " " ++ showHelp l

someTree :: Bst Int
someTree =
  Node (Node Nil 1 Nil) 2 (Node Nil 3 Nil)
