#Named string format
"The {foo} is {bar}".format(foo='answer', bar=42)

#Conditional Assignment
x = 3 if (y == 1) else 2
x = 3 if (y == 1) else 2 if (y == -1) else 1

(func1 if y == 1 else func2)(arg1, arg2)
x = (class1 if y == 1 else class2)(arg1, arg2)

#Nested list comprehensions and generator expressions:
[(i,j) for i in range(3) for j in range(i) ]
((i,j) for i in range(4) for j in range(i) )

#Iterate two lists:
[(i,j) for i in zip(A, B)]
for i, j in zip(A, B):
    pass

#Multiplying by a boolean
tag = isSelected ? "select" : ""
tag = "select" if isSelected else ""
tag = "select"* isSelected

#function with multipl value return
def circle(r):
    circumference = 3.14* 2 * r
    area = 3.14 * r * r
    return circumference, area

#awesome ZIP
"string".encode('zlib')
"string".decode('zlib')

#Creating enums
FOO, BAR, BAZ = range(3)
RED, GREEN, BLUE, YELLOW = (255,0,0), (0,255,0), (0,0,255), (0,255,255)


#Flat List
l = [[1, 2, 3], [4, 5], [6], [7, 8, 9]]
sum(l, [])

#Using True|False as indexer
purchase_result = False
result = ['Your transaction failed','Your transaction is done!'][purchase_result]

#Get maximum element with its index
(m,i) = max((v,i) for i,v in enumerate(values))

#   C#
int? maxVal = null; //nullable so this works even if you have all super-low negatives
int index = -1;
for (int i = 0; i < anArray.Length; i++)
{
  int thisNum = anArray[i];
  if (!maxVal.HasValue || thisNum > maxVal.Value)
  {
    maxVal = thisNum;
    index = i;
  }
}

var max = anArray.Select((value, index) => new {value, index})
                 .OrderByDescending(vi => vi.value)
                 .First();

 int maxValue = anArray.Max();
 int maxIndex = anArray.ToList().IndexOf(maxValue);









###################################
#zip string inython
def zip_str(string_data):
    try: return string_data.encode('zlib')
    except: pass

#Zip in Java
    private static void compressGzipFile(String string_data, String gzipFile) {
        try {
            FileInputStream fis = new FileInputStream(string_data);
            FileOutputStream fos = new FileOutputStream(gzipFile);
            GZIPOutputStream gzipOS = new GZIPOutputStream(fos);
            byte[] buffer = new byte[1024];
            int len;
            while((len=fis.read(buffer)) != -1){
                gzipOS.write(buffer, 0, len);
            }
            //close resources
            gzipOS.close();
            fos.close();
            fis.close();
        } catch (IOException e) {
            e.printStackTrace();
        }

    }













#Zip multiple file
import zipfile
files = ["C:/srcfile1.txt", "C:/srcfile2.txt", "C:/srcfile3.txt"]
zip = zipfile.ZipFile("c:/data.zip")
for fn in files:
    zip.write(fn)
zip.close()

#Zip multiple file is Java
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.zip.ZipEntry;
import java.util.zip.ZipOutputStream;

public class CreateZipFileFromMultipleFilesWithZipOutputStream {
    public static void main(String[] args) {
        String zipFile = "C:/archive.zip";
        String[] srcFiles = { "C:/srcfile1.txt", "C:/srcfile2.txt", "C:/srcfile3.txt"};
        try {
            byte[] buffer = new byte[1024];
            FileOutputStream fos = new FileOutputStream(zipFile);
            ZipOutputStream zos = new ZipOutputStream(fos);
            for (int i=0; i < srcFiles.length; i++) {
                File srcFile = new File(srcFiles[i]);
                FileInputStream fis = new FileInputStream(srcFile);
                zos.putNextEntry(new ZipEntry(srcFile.getName()));
                int length;
                while ((length = fis.read(buffer)) > 0) {
                    zos.write(buffer, 0, length);
                }
                zos.closeEntry();
                fis.close();
            }
            zos.close();
        }
        catch (IOException ioe) {
            System.out.println("Error creating zip file: " + ioe);}}}


import timeit
def use_for():
    res = []
    for i in xrange(10):
        res.append(i**2)
    return res
# Measure it since costly_func is a callable without argument
print timeit.timeit(use_for, number=10000)

def costly_func():
     return map(lambda x: x**2, xrange(10))
# Measure it since costly_func is a callable without argument
print timeit.timeit(costly_func, number=10000)

# Measure it using raw statements
print timeit.timeit('map(lambda x: x**2, xrange(10))', number=10000)
print timeit.timeit('[x**2 for x in xrange(10)]', number=10000)